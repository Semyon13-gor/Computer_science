from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Базовый класс для всех моделей
Base = declarative_base()


class Actors(Base):
    __tablename__ = "Actors"
    Name = Column(String)
    Id = Column(Integer, primary_key=True)
    Biography = Column(String)

    movie = relationship('Movies', secondary='Actor_to_movies', back_populates='actor')

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
    actor_id = Column(Integer)


    director = relationship('Directors', back_populates='movie')

    actor = relationship('Actors', secondary='Actor_to_movies', back_populates='movie')

class Actor_to_movies(Base):
    __tablename__ = "Actor_to_movies"
    actor_id = Column(Integer, ForeignKey('Actors.Id'), primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'), primary_key=True)


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


