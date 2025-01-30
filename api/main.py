from flask import Flask, request, jsonify
import psycopg2
from flask_cors import CORS, cross_origin
import time

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:8000", "http://localhost:8000"]}})  # Allow local origins

# PostgreSQL Datenbank Konfiguration
DB_CONFIG = {
    "dbname": "recipe_db",
    "user": "admin",
    "password": "bo2003wel",
    "host": "localhost",
    "port": "5432"
}

# Funktion um eine Verbindung zur Datenbank herzustellen
def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Database connection established.")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

conn = get_db_connection()  # Verbindung zur Datenbank herstellen

@app.route('/search', methods=['GET'])  # GET Methode für die Suchfunktion
@cross_origin(origins=["http://127.0.0.1:8000", "http://localhost:8000"])  # Enable CORS for this route
def search():
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500  # Fehlermeldung, wenn keine Verbindung zur Datenbank besteht

    ingredient_str = request.args.get('ingredients')  # Suchparameter aus der URL abrufen
    
    if not ingredient_str:
        return jsonify({"error": "No ingredients provided"}), 400  # Fehlermeldung, wenn keine Suchparameter angegeben wurden

    ingredients = [ing.strip() for ing in ingredient_str.split(',')]  # Suchparameter in eine Liste umwandeln

    try:
        start_time = time.time()
        
        # SQL-Abfrage: Use ILIKE for case-insensitive pattern matching
        query = """
            SELECT title, ingredients, directions
            FROM recipes
            WHERE ingredients ILIKE ALL (%s)
            LIMIT 5
        """
        ingredients_array = [f"%{ingredient}%" for ingredient in ingredients]  # Add wildcards for pattern matching
        cursor = conn.cursor()  # Cursor erstellen
        cursor.execute(query, (ingredients_array,))  # SQL-Abfrage ausführen
        results = cursor.fetchall()  # Ergebnisse abrufen

        if not results:
            return jsonify({"message": "No matching recipes found"}), 404  # Fehlermeldung, wenn keine passenden Rezepte gefunden wurden

        # Ergebnisse in ein JSON-Objekt umwandeln und zurückgeben
        recipes = [
            {"title": row[0], "ingredients": row[1], "directions": row[2]} 
            for row in results
        ]
        
        end_time = time.time()  # Capture the end time of the query execution
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Query executed in {execution_time:.4f} seconds.")  # Log the execution time
        
        return jsonify({"recipes": recipes}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Mainfunktion, um die Flask-Anwendung zu starten
if __name__ == "__main__":
    app.run(debug=True)