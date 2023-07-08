from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__, static_url_path="/static")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/testing.db"
app.config["SECRET_KEY"] = "testkey"

db.init_app(app)

from hotelmaster import routes