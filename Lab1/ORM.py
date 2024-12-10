from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Базовый класс для всех моделей
Base = declarative_base()

class Directors(Base):
    __tablename__ = "directors"
    name = Column(String)
    id = Column(Integer, primary_key=True)
    gender = Column(Integer)
    uid = Column(Integer)
    department = Column(String)

    movie = relationship('Movies', back_populates='director')

class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    original_title = Column(String)
    budget = Column(Integer)
    popularity = Column(Integer)
    release_date = Column(String)
    revenue = Column(Integer)
    title = Column(String)
    vote_average = Column(Float)
    vote_count = Column(Integer)
    overview = Column(String)
    tagline = Column(String)
    uid = Column(Integer)
    director_id = Column(Integer, ForeignKey('directors.id'))

    director = relationship('Directors', back_populates='movie')


class Sqlite_sequence:
    __tablename__ = "sqlite_sequence"
    name = Column(String)
    seq = Column(Integer)


def setup_database(database_path="sqlite:///movies.sqlite"):
    engine = create_engine(database_path)
    Base.metadata.create_all(engine)
    return engine

# Создание сессии
def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()


