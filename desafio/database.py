from main import app
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DATABASE = os.getenv('DATABASE')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app, model_class=Base)

class Partner(db.Model):
    __tablename__ = 'partners'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    tradingName: Mapped[str] = mapped_column(db.String, nullable=False)
    ownerName: Mapped[str] = mapped_column(db.String, nullable=False)
    document: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    coverageArea: Mapped[object]

