from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///lojaweb1.db'
app.config["SECRET_KEY"]='28d16c04'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from loja.admin import rotas