from flask import Flask, jsonify
from urllib.parse import quote
# from model.user_db import User_DB

# create the extension
# db = SQLAlchemy()
from backend.test_db import db
from model.user_db import User_DB


def create_app():
    app = Flask(__name__)

    # configuration of connection
    # need to encode password with special
    password = 'D3f@ult!'
    encoded_password = quote(password)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc://sa:{encoded_password}@00ICT0000019\\SQL2014/POS?driver=ODBC+Driver+17+for+SQL+Server'
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
                'Lastname': d.Lastname,
            })

        return jsonify({'data': data_json}), 200
    return app
