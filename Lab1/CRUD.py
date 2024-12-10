from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM import setup_database, create_session, Directors, Movies  # Подключаем модели из ORM

# Инициализация базы данных

engine = setup_database("sqlite:///movies.sqlite")
session = create_session(engine)


#Create
def add_director(name, gender=2, department="Directing", uid=0):
    new_direct = Directors(name=name, gender=gender, department=department, uid=uid)
    session.add(new_direct)
    session.commit()
    print(f"director {name} have id {new_direct.id}")
    return new_direct.id

def add_movie(director_id=0, original_title="", budget=0,popularity=0, release_date="2000-01-01",revenue=0, title="",vote_average=0.0,vote_count=0,overview="",tagline="",uid=0):
    new_movie = Movies(original_title=original_title, budget=budget,popularity=popularity,release_date=release_date,revenue=revenue,title=title,vote_average=vote_average,vote_count=vote_count,overview=overview,tagline=tagline,uid=uid,director_id=director_id)
    session.add(new_movie)
    session.commit()
    print(f"movie {original_title} has {new_movie.id}")
    return new_movie.id

#READ

def get_director_by_id(direct_id):
    direct = session.query(Directors).filter_by(id=direct_id).first()
    if direct:
        return direct
    else:
        print(f"Director with ID {direct_id} not found")
        return None

def get_movie_by_id(movie_id):
    movie = session.query(Movies).filter_by(id=movie_id).first()
    if movie:
        print(f"Movie ID {movie_id}, Title: {movie.title}, release data: {movie.release_date}")
        return movie
    else:
        print(f"Movie with ID {movie_id} not found")

def get_all_movies():
    movies = session.query(Movies).all()
    for movie in movies:
        print(f"Movie ID {movie.id}, Title: {movie.title}, release data: {movie.release_date}")
    return movies

def get_movie_by_title(title):
    movie = session.query(Movies).filter_by(title=title).first()
    director = get_director_by_id(movie.director_id)
    if(movie):
        print(f"Movie: {movie.title}, release data: {movie.release_date}, director name: {director.name}")
    else:
        print(f"Not found movie with title {title}")

def get_movies_by_year(year):
    movies = session.query(Movies).filter(Movies.release_date.contains(str(year))).all()
    if movies and (len(str(year)) == 4):
        for movie in movies:
            print(f"Title {movie.title}, release data {movie.release_date}, director: {get_director_by_id(movie.director_id).name}")
    else:
        print(f"Movie release in {year} not found")

def get_first_movie_every_directors():
    directors = session.query(Directors).all()
    for director in directors:
        movie = session.query(Movies).filter_by(director_id=director.id).first()
        if movie:
            print(f"Director name: {director.name}, Director id {director.id}, Movie title: {movie.title}")
        else:
            print(f"Director name: {director.name}, Director id {director.id}, Movie title: not found")
def get_movies_by_year_and_vote_average(year, vote_average):
    movies = session.query(Movies).filter(Movies.release_date.contains(str(year)), Movies.vote_average >= float(vote_average)).all()
    if movies and (len(str(year)) == 4):
        for movie in movies:
            print(f"Movie {movie.title}, vote average {movie.vote_average}, release date {movie.release_date}")
    else:
        print("Movies not found")
def get_movies_by_director(direct_id):
    movies = session.query(Movies).filter_by(director_id=direct_id).all()
    director = get_director_by_id(direct_id)
    for movie in movies:
        print(f"{movie.title} by {director.name}")
    return movies

#UPDATE

def update_director_name(direct_id, new_name):
    director = session.query(Directors).filter_by(id=direct_id).first()
    if director:
        director.name = new_name
        session.commit()
        print(f"Director ID {direct_id} updated to '{new_name}'")
        return director
    else:
        print(f"Director with ID {direct_id} not found")
        return None

def update_movie_title(movie_id, new_title):
    movie = session.query(Movies).filter_by(id=movie_id).first()
    if movie:
        movie.title = new_title
        session.commit()
        print(f"Movie with ID {movie_id} updated to '{new_title}'")
        return movie
    else:
        print(f"Movie with ID {movie_id} not found")
        return None

#DELETE

def delete_director(direct_id):
    director = session.query(Directors).filter_by(id=direct_id).first()
    if director:
        movies = session.query(Movies).filter_by(director_id=director.id).all()
        for movie in movies:
            session.delete(movie)
            session.commit()
        session.delete(director)
        session.commit()
        print(f"Director ID {direct_id} deleted")
    else:
        print(f"Director with ID {direct_id} not found")

def delete_movie(movie_id):
    movie = session.query(Movies).filter_by(id=movie_id).first()
    if movie:
        session.delete(movie)
        session.commit()
        print(f"Movie ID {movie_id} deleted")
    else:
        print(f"Movie with ID {movie_id} not found")

if __name__ == "__main__":
    get_movies_by_year_and_vote_average(1999, 7.5)









