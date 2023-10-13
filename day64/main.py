from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from models import DataBaseMovies, Movie
from models import FormEdit
from models import FormAdd
from models import FormSearchName
from get_movie_api import GetMovie

m_db = DataBaseMovies()
app = m_db.app
bootstrap = Bootstrap5(app=app)

@app.route("/")
def home():
    top_movies = m_db.getData()
    return render_template("index.html", bootstrap = bootstrap, top_movies = top_movies)


@app.route("/add", methods=['POST', 'GET'])
def add_movie_1():
    if request.method == 'GET':
        print("get")
        form = FormAdd()
        return render_template('add.html', form = form)
    elif request.method == 'POST':
        print('Post')
        x = request.form.to_dict()
        new_movie = Movie(
            title = x['title'],
            year = x['year'],
            description = x['description'],
            rating = x['rating'],
            ranking = x['ranking'],
            review = x['review'],
            img_url = x['img_url']
        )
        m_db.add(movie= new_movie)
        flash('Adding successful, returning to the main page')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))
        


@app.route("/edit/<in_id>", methods = ['GET', 'POST'])
def edit(in_id):
    if request.method == 'GET':
        return render_template("edit.html", form = FormEdit())
    elif request.method == 'POST':
        rating = request.form.get('rating')
        review = request.form.get('review')
        m_db.updateByID(in_id=in_id, rating = rating, review = review)
        return redirect(url_for('home'))


@app.route("/<in_id>")
def delete(in_id):
    m_db.deleteByID(in_id=in_id)
    return redirect(url_for('home'))


@app.route("/search", methods = ['GET','POST'])
def add_movie_2():
    if request.method == 'GET':
        return render_template("add.html", form = FormSearchName())
    elif request.method == 'POST':
        movie_name_searched = request.form.get('title')
        get_movie = GetMovie()
        movies_dict = get_movie.get_movieByName(name=movie_name_searched)
        return render_template("search.html", movies_dict = movies_dict)
    else:
        flash('Something went wrong, redirecting to the home page...')
        return redirect(url_for('home'))
    

@app.route('/add_selected/<id>')
def add_selected_movie(id):
    get_movie = GetMovie()
    movie_obj = get_movie.get_movieById(id = id)
    if movie_obj != None:
    #print(movie_obj)
        base_url_for_img ="https://image.tmdb.org/t/p/original" #instead of original attr. you can try wSize format look for more inf.
                                                            #https://developer.themoviedb.org/docs/image-basics
        new_movie = Movie(
                title = movie_obj['original_title'],
                year = movie_obj['release_date'],
                review = movie_obj['tagline'],
                description = movie_obj['overview'],
                ranking = movie_obj['vote_average'],
                img_url = base_url_for_img + movie_obj['poster_path']
            )
        m_db.add(new_movie)
    else:
        flash("Something went wrong...")
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True, port=8000)
