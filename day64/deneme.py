from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, VARCHAR, INTEGER, FLOAT,  DATETIME


db = SQLAlchemy()

class Movie(db.Model):
    id = Column(INTEGER, primary_key=True, autoincrement=1)
    title = Column(VARCHAR(25), nullable=False, unique=True)
    year = Column(INTEGER, nullable=False)
    description = Column(VARCHAR(50), nullable=False, unique=True)
    rating = Column(FLOAT, nullable=False)
    ranking = Column(FLOAT, nullable=False)
    review = Column(VARCHAR, nullable=True, server_default="No review availale at the moment")
    img_url = Column(VARCHAR, nullable=False)
    

app = Flask(__name__)
app.config['SECRET_KEY'] = 'justarandomkey'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///deneme.db"
db.init_app(app)

new_movie = Movie(
    title = "Drive",
    year = 2011,
    description ="A mysterious Hollywood stuntman and mechanic moonlights as a getaway driver and finds himself in trouble when he helps out his neighbor in this action drama." ,
    rating = 7.5,
    ranking = 0,
    review = "Loved it",
    img_url = "https://www.shortlist.com/media/images/2019/05/the-30-coolest-alternative-movie-posters-ever-2-1556670563-K61a-column-width-inline.jpg"
)

with app.app_context():
    db.session.add(new_movie)
    db.session.commit()
