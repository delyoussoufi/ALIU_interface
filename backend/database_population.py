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