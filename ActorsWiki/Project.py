from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from ORM import Base, Actors, Movies, Actor_to_movies

app = Flask(__name__)


DATABASE_URI = "sqlite:///movies.sqlite"
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def index():
    search_query = request.args.get('search', '').strip()
    if search_query:

        actors = session.query(Actors).filter(Actors.Name.ilike(f'%{search_query}%')).all()
    else:

        actors = session.query(Actors).all()
    return render_template('index.html', actors=actors, search_query=search_query)


@app.route('/actor/<int:actor_id>')
def actor_detail(actor_id):
    actor = session.query(Actors).filter_by(Id=actor_id).first()
    if not actor:
        return "Актер не найден", 404


    movies = session.query(Movies).join(Actor_to_movies).filter(Actor_to_movies.actor_id == actor_id).all()
    return render_template('actor_detail.html', actor=actor, movies=movies)




@app.route('/actor/add', methods=['GET', 'POST'])
def add_actor():
    if request.method == 'POST':

        name = request.form['name']
        biography = request.form['biography']


        new_actor = Actors(Name=name, Biography=biography)
        session.add(new_actor)
        session.commit()


        return redirect(url_for('actor_detail', actor_id=new_actor.Id))


    return render_template('add_actor.html')

@app.route('/actor/<int:actor_id>/edit', methods=['GET', 'POST'])
def edit_actor(actor_id):
    actor = session.query(Actors).filter_by(Id=actor_id).first()
    if not actor:
        return "Актер не найден", 404

    if request.method == 'POST':

        actor.Name = request.form['name']
        actor.Biography = request.form['biography']


        movie_ids = request.form.getlist('movies')
        for movie_id in movie_ids:
            movie = session.query(Movies).filter_by(id=movie_id).first()
            if movie and movie not in actor.movie:
                actor.movie.append(movie)

        session.commit()
        return redirect(url_for('actor_detail', actor_id=actor.Id))


    search_query = request.args.get('search', '').strip()
    if search_query:

        all_movies = session.query(Movies).filter(Movies.title.ilike(f'%{search_query}%')).all()
    else:

        all_movies = session.query(Movies).all()

    return render_template('edit_actor.html', actor=actor, all_movies=all_movies)
if __name__ == '__main__':
    app.run(debug=True)