from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'my-undisclosed-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost/stackoverflow-lite'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt = Bcrypt(app)


from app import routes
