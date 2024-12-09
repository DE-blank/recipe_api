from flask import Flask, request, jsonify
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes by default

# Database connection setup
DB_CONFIG = {
    "dbname": "recipe_db",
    "user": "admin",
    "password": "bo2003wel",
    "host": "localhost",
    "port": "5432"
}

# Establish database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("Database connection established.")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

conn = get_db_connection()

@app.route('/search', methods=['GET'])
def search():
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500

    ingredient_str = request.args.get('ingredients')
    
    if not ingredient_str:
        return jsonify({"error": "No ingredients provided"}), 400

    ingredients = [ing.strip() for ing in ingredient_str.split(',')]

    try:
        query = f"""
        SELECT title, ingredients, directions
        FROM recipes
        WHERE {' AND '.join([f"ner ILIKE %s"] * len(ingredients))}
        LIMIT 5
        """
        cursor = conn.cursor()
        cursor.execute(query, tuple([f'%{ingredient}%' for ingredient in ingredients]))
        results = cursor.fetchall()

        if not results:
            return jsonify({"message": "No matching recipes found"}), 404

        recipes = [
            {"title": row[0], "ingredients": row[1], "directions": row[2]} 
            for row in results
        ]
        return jsonify({"recipes": recipes}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()