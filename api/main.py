from flask import Flask, request, jsonify # Flask-Modul importieren
import psycopg2 # PostgreSQL-Modul importieren
from flask_cors import CORS # Cors-Modul importieren

app = Flask(__name__)
CORS(app) 

# PostgreSQL Datenbank Konfiguration
DB_CONFIG = {
    "dbname": "recipe_db",
    "user": "admin",
    "password": "bo2003wel",
    "host": "localhost",
    "port": "5432"
}

# funktion um eine Verbindung zur Datenbank herzustellen
def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Database connection established.")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

conn = get_db_connection() # Verbindung zur Datenbank herstellen

@app.route('/search', methods=['GET']) # GET Methode für die Suchfunktion
def search():
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500 # Fehlermeldung, wenn keine Verbindung zur Datenbank besteht

    ingredient_str = request.args.get('ingredients') # Suchparameter aus der URL abrufen
    
    if not ingredient_str:
        return jsonify({"error": "No ingredients provided"}), 400 # Fehlermeldung, wenn keine Suchparameter angegeben wurden

    ingredients = [ing.strip() for ing in ingredient_str.split(',')] # Suchparameter in eine Liste umwandeln

    try:
        # SQL Query um Rezepte zu suchen, die die angegebenen Zutaten enthalten
        query = f"""
        SELECT title, ingredients, directions
        FROM recipes
        WHERE {' AND '.join([f"ner ILIKE %s"] * len(ingredients))}
        LIMIT 5
        """
        cursor = conn.cursor() # Cursor erstellen
        cursor.execute(query, tuple([f'%{ingredient}%' for ingredient in ingredients])) # SQL Query ausführen
        results = cursor.fetchall() # Ergebnisse abrufen

        if not results:
            return jsonify({"message": "No matching recipes found"}), 404 # Fehlermeldung, wenn keine passenden Rezepte gefunden wurden

        # Ergebnisse in ein JSON-Objekt umwandeln und zurückgeben
        recipes = [
            {"title": row[0], "ingredients": row[1], "directions": row[2]} 
            for row in results
        ]
        return jsonify({"recipes": recipes}), 200

    # Fehlerbehandlung
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Mainfunktion, um die Flask-Anwendung zu starten
if __name__ == "__main__":
    app.run()