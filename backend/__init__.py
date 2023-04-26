import os
from flask import Flask, jsonify
from urllib.parse import quote
from backend.test_db import db
from model.user_db import User_DB

# using environment variables for credentials
from dotenv import load_dotenv
load_dotenv()

# Access environment variables
db_username = os.getenv('DB_USERNAME')
db_password = quote(os.getenv('DB_PASSWORD'))  # encoded password special
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc://{db_username}:{db_password}@{db_host}/{db_name}?driver=ODBC+Driver+17+for+SQL+Server'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialized the db in the app
    db.init_app(app)

    # sample route
    @app.route('/')
    def hello_world():
        data = User_DB.query.all()
        data_json = []

        for d in data:
            data_json.append({
                'id': d.UserId,
                'Firstname': d.Firstname,
                'Middlename': d.Middlename,
                'Lastname': d.Lastname
            })

        return jsonify({'data': data_json}), 200
    return app
