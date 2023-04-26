from urllib.parse import quote
# from model.user_db import User_DB
from backend import create_app

app = create_app()

if __name__ == '__app__':
    app.run(debug=True)
