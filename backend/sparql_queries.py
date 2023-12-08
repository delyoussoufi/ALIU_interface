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
    SELECT ?ArtObjectID ?ArtObjectName ?ArtObjectDescription ?OwnedByID ?OwnedByName ?ImageURL
        ?CreatorName ?DateOfCreation ?Material ?Location ?Height ?Width ?Genre ?Event ?Source ?Origin ?Exhibition
    WHERE {
        ?artObject wdt:P31 wd:Q3305213;  # Instances of painting
                wdt:P127 ?ownedby;       # Known owner
                wdt:P18 ?image.          # Image of the art object

        ?ownedby wdt:P1840 wd:Q30335959.  # Owner was ALIU Red Flag

        BIND(STRAFTER(STR(?artObject), "http://www.wikidata.org/entity/") AS ?ArtObjectID)
        OPTIONAL { ?artObject rdfs:label ?ArtObjectName. FILTER(LANG(?ArtObjectName) = "en") }
        OPTIONAL { ?artObject schema:description ?ArtObjectDescription. FILTER(LANG(?ArtObjectDescription) = "en") }
        OPTIONAL { ?ownedby rdfs:label ?OwnedByName. FILTER(LANG(?OwnedByName) = "en") }

        OPTIONAL { ?artObject wdt:P571 ?DateOfCreation. }
        OPTIONAL { ?artObject wdt:P170 ?creator. ?creator rdfs:label ?CreatorName. FILTER(LANG(?CreatorName) = "en") }
        OPTIONAL { ?artObject wdt:P186 ?material. ?material rdfs:label ?Material. FILTER(LANG(?Material) = "en") }
        OPTIONAL { ?artObject wdt:P276 ?location. ?location rdfs:label ?Location. FILTER(LANG(?Location) = "en") }
        OPTIONAL { ?artObject wdt:P2048 ?Height. }
        OPTIONAL { ?artObject wdt:P2049 ?Width. }
        OPTIONAL { ?artObject wdt:P136 ?genre. ?genre rdfs:label ?Genre. FILTER(LANG(?Genre) = "en") }
        OPTIONAL { ?artObject wdt:P793 ?event. ?event rdfs:label ?Event. FILTER(LANG(?Event) = "en") }
        OPTIONAL { ?artObject wdt:P1343 ?source. ?source rdfs:label ?Source. FILTER(LANG(?Source) = "en") }
        OPTIONAL { ?artObject wdt:P495 ?origin. ?origin rdfs:label ?Origin. FILTER(LANG(?Origin) = "en") }
        OPTIONAL { ?artObject wdt:P608 ?exhibition. ?exhibition rdfs:label ?Exhibition. FILTER(LANG(?Exhibition) = "en") }

        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]"}
    }
    GROUP BY ?ArtObjectID ?ArtObjectName ?ArtObjectDescription ?OwnedByID ?OwnedByName ?ImageURL
            ?CreatorName ?DateOfCreation ?Material ?Location ?Height ?Width ?Genre ?Event ?Source ?Origin ?Exhibition
    ORDER BY ?ArtObjectID
    LIMIT 100

    """)
    sparql.setReturnFormat(JSON)
    return fetch_data_with_retries(sparql)