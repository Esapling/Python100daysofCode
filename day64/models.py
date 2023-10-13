from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, VARCHAR, INTEGER, FLOAT
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, URLField
from wtforms.validators import DataRequired, URL
from sqlalchemy import desc

db = SQLAlchemy()

class Movie(db.Model):
    id = Column(INTEGER, primary_key=True)
    title = Column(VARCHAR(25), nullable=False, unique=True)
    year = Column(INTEGER, nullable=False)
    description = Column(VARCHAR(50), nullable=False, unique=True)
    rating = Column(FLOAT, default=0)
    ranking = Column(INTEGER, nullable=False)
    review = Column(VARCHAR, nullable=True, server_default="No review availale at the moment")
    img_url = Column(VARCHAR, nullable=False)

class DataBaseMovies:
    def __init__(self) -> None:
        self.db = db
        self.app = Flask(__name__)
        self.create_db()

    def create_db(self):
        self.app.config['SECRET_KEY'] = 'justarandomkey'
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies.db"
        self.db.init_app(self.app)
        with self.app.app_context():
            self.db.create_all()

    def getData(self):
        with self.app.app_context():
            data = self.db.session.execute(self.db.select(Movie).order_by(desc(Movie.ranking))).scalars()
            return data.fetchall()
        
    def add(self,movie: Movie):
        with self.app.app_context():
            self.db.session.add(movie)
            self.db.session.commit()

    def updateByID(self,in_id, **kwargs):
        with self.app.app_context():
            #self.db.session.query(self.db.select(Movie).where(Movie.id == in_id)).update(kwargs)
            self.db.session.query(Movie).filter_by(id= in_id).update(kwargs)
            self.db.session.commit()

    def deleteByID(self, in_id: int):
        with self.app.app_context():
            movie_deleted = self.db.session.execute(self.db.select(Movie).where(Movie.id == in_id)).scalar()
            self.db.session.delete(movie_deleted)
            self.db.session.commit()


class FormEdit(FlaskForm):
    rating = FloatField("Your Rating out of 10 e.g 6.4", validators=[DataRequired(),])
    review = StringField("Your review", validators=[DataRequired(),])
    submit = SubmitField("Submit")

class FormAdd(FormEdit):
    title = StringField("Movie Title", validators=[DataRequired()])
    description = StringField("Movie Description", validators=[DataRequired()])
    year =FloatField("Movie release year", validators=[DataRequired()])
    ranking =FloatField("Movie Ranking", validators=[DataRequired()])
    img_url = URLField("Movie image url", validators=[URL()])
    submit = SubmitField("Submit")


class FormSearchName(FlaskForm):
    title = StringField("Enter movie title", validators=[DataRequired()])
    submit = SubmitField("Submit")
    