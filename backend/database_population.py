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