#!/bin/bash

HTML_FILE="index.html"
HTML_DIR="/Users/bruno/inf_abschluss/frontend"
PORT=8000
FLASK_APP_PATH="/Users/bruno/inf_abschluss/api/main.py"

error_exit() {
    echo "$1"
    exit 1
}

echo "Activating virtual environment..."
source /Users/bruno/inf_abschluss/venv/bin/activate || error_exit "Failed to activate virtual environment."

echo "Starting PostgreSQL..."
brew services start postgresql || error_exit "Failed to start PostgreSQL."

echo "Starting Flask app in a new terminal window..."
osascript <<EOF
tell application "Terminal"
    do script "source /Users/bruno/inf_abschluss/venv/bin/activate && python $FLASK_APP_PATH"
end tell
EOF
sleep 

echo "Starting Python HTTP server to serve $HTML_FILE..."
cd "$HTML_DIR" || error_exit "Failed to navigate to $HTML_DIR"
python3 -m http.server "$PORT" & 
sleep 2 

echo "Opening browser to view the HTML file..."
open "http://localhost:$PORT/$HTML_FILE" || error_exit "Failed to open browser."

echo "All processes started successfully."