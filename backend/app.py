from flask import Flask, jsonify, request
from sqlite3 import connect as sqlite_connect
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return sqlite_connect('artdatabase.db')

@app.route('/artobjects/', methods=['GET'])
def get_art_objects():
    query = request.args.get('query', '')  # Get the query parameter
    conn = get_db_connection()
    cur = conn.cursor()

    if query:
        # Modify this query to search across multiple fields
        search_query = f"%{query}%"
        cur.execute("""
            SELECT * FROM t_art_objects 
            WHERE ArtObjectName LIKE ?
            OR ArtObjectID LIKE ?
            OR ArtObjectDescription LIKE ?
            OR CreatorName LIKE ?

            """, (search_query, search_query, search_query, search_query))
    else:
        cur.execute('SELECT * FROM t_art_objects')

    art_objects = cur.fetchall()
    cur.close()
    conn.close()

    art_objects_list = [dict(zip([column[0] for column in cur.description], ao)) for ao in art_objects]
    return jsonify(art_objects_list)