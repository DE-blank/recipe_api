#!/bin/bash

echo "Activating virtual environment..."
source /Users/bruno/inf_abschluss/venv/bin/activate || { echo "Failed to activate venv"; exit 1; }

echo "Starting PostgreSQL..."
brew services start postgresql || { echo "Failed to start PostgreSQL"; exit 1; }

echo "Running Flask app..."
python api/main.py || { echo "Failed to run Flask app"; exit 1; }

echo "All processes started successfully."