import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DATABASE = os.getenv('DATABASE')

engine = create_engine(f'mysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

