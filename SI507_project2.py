# Import statements necessary
from flask import Flask, render_template
from movies_tools import *


# Set up application
app = Flask(__name__)
data = None

# Routes
@app.route('/')
def home():
    return '<h1> {} movies recorded. </h1>'.format(len(data))

@app.route('/movies/ratings/')
def movie_title_rating():

    return render_template('ratings.html', masterlist = data[1:7] )

if __name__ == '__main__':
    data = process("movies_clean.csv")
    app.run()
