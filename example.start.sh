#!/bin/bash
source .env/bin/activate

export FLASK_ENV=development
export FLASK_APP=app.py
export FLASK_SECRET_KEY=

flask run