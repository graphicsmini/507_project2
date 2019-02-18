# Import statements necessary
from flask import Flask, render_template
import movies_tools 
import csv

# Set up application
app = Flask(__name__)


# Open movies_clean.csv file
with open("movies_clean.csv", "r") as f:
	reader = csv.reader(f)
	data = []
	for i in reader:
		data.append(i)


# Routes
@app.route('/')
def home():

    return '<h1> <number> movies recorded. </h1>'

@app.route('/movies/ratings/')
def movie_title_rating():
    title = Movie(number)
    rating = Movie(rating)

    return render_template('values.html',movie_title=title,movie_rating=rating)






if __name__ == '__main__':
    app.run()
