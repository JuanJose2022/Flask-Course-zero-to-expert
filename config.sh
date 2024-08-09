#!bin/bash

export FLASK_ENV=$1
echo "FLASK_ENV set to $FLASK_ENV"

export FLASK_APP=$2
echo "FLASK_APP set to $FLASK_APP"

# On terminal: bash -c "source ./config.sh development"
# Run all tests: python -m unittest discover -s tests
#Run a specific test: python -m unittest tests/test_app.py

#Run flask: flask --app main.py run
   