from SPARQLWrapper import SPARQLWrapper, JSON
import time
from urllib.error import HTTPError
import random
def fetch_data_with_retries(sparql, max_retries=5, initial_backoff=2):
    for retry in range(max_retries):
        try:
            results = sparql.query().convert()
            return results['results']['bindings']
        except Exception as e:
            if isinstance(e, HTTPError) and e.code == 429:  # Too Many Requests
                # Exponential backoff with jitter
                backoff = initial_backoff * (2 ** retry) + random.uniform(0, 1)
                print(f"Rate limit hit, backing off for {backoff} seconds...")
                time.sleep(backoff)
            else:
                raise
    raise Exception("Max retries exceeded")

def fetch_art_objects():
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery("""
    SELECT ?artObject ?artObjectLabel ?artObjectDescription ?ownedby ?ownedbyLabel ?creationDate ?artist ?artistLabel
    WHERE {
        ?artObject wdt:P31 wd:Q3305213 ; # Get items that are instances of painting
        wdt:P127 ?ownedby. #at least one owner is known in Wikidata
        ?ownedby wdt:P1840 wd:Q30335959 . #the owner was ALIU Red Flag   
        OPTIONAL { ?artObject wdt:P571 ?creationDate. } # Get the date of creation of the art object
        OPTIONAL { ?artObject wdt:P170 ?artist. } # Get the artist of the painting

        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]"}
    }
    GROUP BY ?artObject ?artObjectLabel ?artObjectDescription ?ownedby ?ownedbyLabel ?creationDate ?artist ?artistLabel
    ORDER BY ?item
    LIMIT 100

    """)
    sparql.setReturnFormat(JSON)
    return fetch_data_with_retries(sparql)

def fetch_ownership_history(art_object_id):
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    sparql.setQuery(f"""
    SELECT (?owner as ?OwnerID) ?ownerLabel ?ownFrom ?ownUntil ?ownerDescription ?ownerTypeLabel ?acquisitionMethodLabel
    WHERE {{
        wd:{art_object_id} wdt:P127 ?owner.

        OPTIONAL {{
            wd:{art_object_id} p:P127 [ ps:P127 ?owner ; pq:P580 ?ownFrom].
        }}
        OPTIONAL {{
            wd:{art_object_id} p:P127 [ ps:P127 ?owner ; pq:P582 ?ownUntil].
        }}

        # Request the label for the owner entity
        ?owner rdfs:label ?ownerLabel .
        FILTER(LANG(?ownerLabel) = "en")

        OPTIONAL {{ ?owner schema:description ?ownerDescription. FILTER(LANG(?ownerDescription) = "en") }}
        OPTIONAL {{ ?owner wdt:P31 ?ownerType. ?ownerType rdfs:label ?ownerTypeLabel. FILTER(LANG(?ownerTypeLabel) = "en") }}
        OPTIONAL {{ wd:{art_object_id} p:P127 [ ps:P127 ?owner ; pq:P217 ?acquisitionMethod]. ?acquisitionMethod rdfs:label ?acquisitionMethodLabel. FILTER(LANG(?acquisitionMethodLabel) = "en") }}

        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE]" }}
    }}
    GROUP BY ?owner ?ownerLabel ?ownFrom ?ownUntil ?ownerDescription ?ownerTypeLabel ?acquisitionMethodLabel
    LIMIT 100
    """)

    sparql.setReturnFormat(JSON)
    return fetch_data_with_retries(sparql)

