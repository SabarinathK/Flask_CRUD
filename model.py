from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

class Songs (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    

    def __init__(self, name, duration, time):
        self.name = name
        self.duration = duration
        self.time = time


class podcast (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    host=db.Column(db.String(200), nullable=False)
    participants=db.Column(db.String(200), nullable=False)
    

    def __init__(self, name, duration, time,host,participants):
        self.name = name
        self.duration = duration
        self.time = time
        self.host = host
        self.participants = participants
        
        

class audio_book (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    narrator = db.Column(db.String(200), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    time = db.Column(db.Integer, nullable=False)


    def __init__(self, name, author, narrator,duration,time):
        self.name = name
        self.author = author
        self.narrator = narrator
        self.duration = duration
        self.time = time
        
with app.app_context():
    db.create_all()
    