# Documentation for the aliu_interface
## Introduction
ALIU INTERFACE is a specialized database platform focusing on artworks previously identified with an Art Looting Investigation Unit (ALIU) Red Flag status. This designation indicates potential involvement in looting or illegal transactions during World War II. Our platform serves as a resource for researchers, historians, and art professionals, providing detailed information on these specific art objects.
## Backend
### Overview 
This backend application manages an art database, focusing on art objects and their ownership history. It integrates data fetching from Wikidata, storage in a SQLite database, and a Flask API for data access.

### Components
The backend is structured into several key components:

create_schema.sql: SQL script for creating database tables.
create_database.py: Python script to initialize the database.
sparql_queries.py: Contains functions to fetch data using SPARQL queries.
data_population.py: Script for populating the database with fetched data.
app.py: Flask application providing API endpoints.

### Database Schema

Tables:
t_art_objects: Stores comprehensive details about art objects.
t_art_owners: Stores the historical ownership data of each art object.


Table: t_art_objects  

ArtObjectID (TEXT, PRIMARY KEY): A unique identifier for each art object. Typically starts with "Q".  
ArtObjectName (TEXT): The name or title of the art object.  
ArtObjectDescription (TEXT): A detailed description of the art object, including its history, significance, and any other relevant information.  
OwnedByID (TEXT): The identifier of the current owner of the art object.  
OwnedByName (TEXT): The name of the current owner of the art object.  
ImageURL (TEXT): A URL linking to an image of the art object.  
CreatorName (TEXT): The name of the artist or creator of the art object.  
DateOfCreation (TEXT): The date when the art object was created. Stored as text to accommodate various date formats.  
Material (TEXT): The primary materials used in the creation of the art object.  
Location (TEXT): The current location or display venue of the art object.  
Height (DECIMAL): The height of the art object, assumed to be in a consistent unit like centimeters or inches.  
Width (DECIMAL): The width of the art object, also in a consistent unit.  
Genre (TEXT): The genre or category that the art object belongs to.  
Event (TEXT): Any significant event associated with the art object.  
Source (TEXT): The source from where the information about the art object was obtained.  
Origin (TEXT): The original location or provenance of the art object.  
Exhibition (TEXT): Information about any exhibitions where the art object has been displayed.  

Table: t_art_owners  

ArtObjectID (TEXT, REFERENCES t_art_objects(ID)): A reference to the unique identifier of the art object in the t_art_objects table.  
OwnerID (TEXT): The identifier of an individual or entity that has owned the art object.  
OwnerName (TEXT): The name of the owner.  
OwnershipFrom (TEXT): The date from which the ownership started.  
OwnershipUntil (TEXT): The date until which the ownership lasted.  
OwnerDescription (TEXT): A description of the owner, which may include background information or relevance to the art object.  
OwnerType (TEXT): The type of owner, e.g., individual, museum, private collector.  
AcquisitionMethod (TEXT): The method through which the owner acquired the art object.  
PRIMARY KEY (ArtObjectID, OwnerID): A composite primary key ensuring each combination of art object and owner and the date from which the ownership started is unique.  

### Environment Setup and Requirements  

System Requirements  
Operating System: Compatible with Windows, macOS, and Linux.  
Python Version: Python 3.9 or higher.  