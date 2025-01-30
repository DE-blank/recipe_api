#!/bin/bash

# HTML-Datei zum Servieren
HTML_FILE="index.html"
HTML_DIR="/Users/bruno/inf_abschluss/frontend" # Verzeichnis der HTML-Datei
PORT=8000 # Port für den HTTP-Server
FLASK_APP_PATH="/Users/bruno/inf_abschluss/api/main.py"

# Funktion für Fehlerausgabe
error_exit() {
    echo "$1"
    exit 1
}

# Virtuelle Umgebung aktivieren
echo "Activating virtual environment..."
source /Users/bruno/inf_abschluss/venv/bin/activate || error_exit "Failed to activate virtual environment."

# PostgreSQL starten
echo "Starting PostgreSQL..."
brew services start postgresql || error_exit "Failed to start PostgreSQL."

# Flask-App in einem neuen Terminalfenster starten
echo "Starting Flask app in a new terminal window..."
osascript <<EOF
tell application "Terminal"
    do script "source /Users/bruno/inf_abschluss/venv/bin/activate && python $FLASK_APP_PATH"
end tell
EOF
sleep 2 # Warten, bis Flask-Server startet

# HTML-Datei über HTTP-Server bereitstellen
echo "Starting Python HTTP server to serve $HTML_FILE..."
cd "$HTML_DIR" || error_exit "Failed to navigate to $HTML_DIR"
python3 -m http.server "$PORT" & # Server im Hintergrund starten
sleep 2 # Warten, bis der Server hochfährt

# Browser öffnen
echo "Opening browser to view the HTML file..."
open "http://localhost:$PORT/$HTML_FILE" || error_exit "Failed to open browser."

echo "All processes started successfully."