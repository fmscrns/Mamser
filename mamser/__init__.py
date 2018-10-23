from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "fmscrns"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/mamser"
db = SQLAlchemy(app)

from mamser import routes