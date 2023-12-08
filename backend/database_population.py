import time
import logging
import sqlite3
from sqlite3 import Error
from SPARQLWrapper import SPARQLWrapper, JSON
from urllib.error import HTTPError
from sparql_queries import fetch_art_objects, fetch_ownership_history
# Setup basic logging
logging.basicConfig(level=logging.INFO)

# SQLite database setup
def create_connection():
    try:
        conn = sqlite3.connect('artdatabase.db')
        return conn
    except Error as e:
        logging.error(f"Error connecting to SQLite database: {e}")
        return None
    
def insert_art_objects(conn, art_objects_data):
    try:
        cursor = conn.cursor()
        for art_object in art_objects_data:
            art_object_id = art_object['ArtObjectID']['value']
            if not art_object_id.startswith("Q"):
                logging.warning(f"Invalid ID format: {art_object_id}")
                continue

            art_object_name = art_object.get('ArtObjectName', {}).get('value', None)
            art_object_description = art_object.get('ArtObjectDescription', {}).get('value', None)
            owned_by_id = art_object.get('OwnedByID', {}).get('value', None)
            owned_by_name = art_object.get('OwnedByName', {}).get('value', None)
            image_url = art_object.get('ImageURL', {}).get('value', None)
            creator_name = art_object.get('CreatorName', {}).get('value', None)
            date_of_creation = art_object.get('DateOfCreation', {}).get('value', None)
            material = art_object.get('Material', {}).get('value', None)
            location = art_object.get('Location', {}).get('value', None)
            height = art_object.get('Height', {}).get('value', None)
            width = art_object.get('Width', {}).get('value', None)
            genre = art_object.get('Genre', {}).get('value', None)
            event = art_object.get('Event', {}).get('value', None)
            source = art_object.get('Source', {}).get('value', None)
            origin = art_object.get('Origin', {}).get('value', None)
            exhibition = art_object.get('Exhibition', {}).get('value', None)

            cursor.execute('''
                INSERT OR IGNORE INTO t_art_objects (ArtObjectID, ArtObjectName, ArtObjectDescription, OwnedByID, OwnedByName, ImageURL, CreatorName, DateOfCreation, Material, Location, Height, Width, Genre, Event, Source, Origin, Exhibition) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (art_object_id, art_object_name, art_object_description, owned_by_id, owned_by_name, image_url, creator_name, date_of_creation, material, location, height, width, genre, event, source, origin, exhibition))

        conn.commit()
    except Error as e:
        logging.error(f"Error inserting art objects into SQLite database: {e}")

def insert_ownerships(conn, art_object_id, ownership_data):
    try:
        cursor = conn.cursor()
        for ownership in ownership_data:
            owner_id = ownership['OwnerID']['value'].split('/')[-1]
            owner_name = ownership.get('ownerLabel', {}).get('value', None)
            ownership_from = ownership.get('ownershipFrom', {}).get('value', None)
            ownership_until = ownership.get('ownnershipUntil', {}).get('value', None)
            owner_description = ownership.get('ownerDescription', {}).get('value', None)
            owner_type = ownership.get('ownerTypeLabel', {}).get('value', None)
            acquisition_method = ownership.get('acquisitionMethodLabel', {}).get('value', None)

            cursor.execute('''
                INSERT OR IGNORE INTO t_art_owners (ArtObjectID, OwnerID, OwnerName, OwnershipFrom, OwnershipUntil, OwnerDescription, OwnerType, AcquisitionMethod) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (art_object_id, owner_id, owner_name, ownership_from, ownership_until, owner_description, owner_type, acquisition_method))

        conn.commit()
    except Error as e:
        logging.error(f"Error inserting ownerships into SQLite database: {e}")

def fetch_with_backoff(art_object_id):
    attempt = 0
    while attempt < 5:  # Retry up to 5 times
        try:
            return fetch_ownership_history(art_object_id)
        except HTTPError as e:
            if e.code == 429:  # Too Many Requests
                logging.warning("Rate limit hit, backing off...")
                time.sleep(2 ** attempt)  # Exponential backoff
                attempt += 1
            else:
                raise
        except Exception as e:
            logging.error(f"Error fetching data for {art_object_id}: {e}")
            raise

def populate_database():
    conn = create_connection()
    if conn is None:
        return

    try:
        art_objects_data = fetch_art_objects()
        insert_art_objects(conn, art_objects_data)
        logging.info("Art objects inserted successfully.")
        for i, art_object in enumerate(art_objects_data, start=1):
            art_object_id = art_object['ArtObjectID']['value']
            ownership_data = fetch_with_backoff(art_object_id)
            if ownership_data:
                insert_ownerships(conn, art_object_id, ownership_data)

            if i % 100 == 0:  # Logging progress every 100 art objects
                logging.info(f"Processed {i} art objects.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

    finally:
        conn.close()
        logging.info("Database connection closed.")

if __name__ == '__main__':
    populate_database()
