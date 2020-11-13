import pandas as pd
import re
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
import sqlite3
import csv
from shapely import geometry
import shapely.wkt

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

base = declarative_base()
class Covid_airport(base):
    __tablename__ = 'covid_airport'
    id = Column(String, primary_key=True)
    aggregation_method = Column(String)
    date = Column(Date)
    version = Column(Float)
    airport_name = Column(String)
    percent_of_baseline = Column(Integer)
    centroid = Column(Integer)
    city = Column(String)
    state = Column(String)
    iso_3166_2 = Column(String)
    country = Column(String)
    geography = Column(Integer)


engine= create_engine("sqlite:///covid.db", echo=True)
base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()


session.close()  # Close the connection
df = pd.read_csv("covid_data_airport.csv")
file_name = 'covid_data_airport'
df['Centroid'] = df['Centroid'].str.replace(r'[^(]*\(|\)[^)]*', '', regex=True)
df[['x', 'y']] = df.Centroid.str.split(" ", expand=True)
df['Geography'] = df['Geography'].str.replace(r'[^(]*\(|\)[^)]*', '', regex=True)
df[['x1', 'y1']] = df.Centroid.str.split(" ", expand=True)


#polygon = geometry.Polygon(['x1', 'y1'])
P = shapely.wkt.loads(['x1', 'y1'])
print(P)

df.to_sql(con=engine, index_label='id', name=Covid_airport.__tablename__, if_exists='replace')

