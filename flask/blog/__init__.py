from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cb364e81ed836bb9769e7fb78dbd6ec1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sql:///site.db'
db = SQLAlchemy(app)

from flask import routes
