import csv

# Define a class Movie that accepts as constructor input one row of the movies_clean.csv file.

class Movie:
    def __init__(self, row):
        self.title = row[0]
        self.rating = row[6]

    def __str__(self):
        return "{} | {}".format(self.title, self.rating)

def process(file):
    with open(file, "r") as f:
    	reader = csv.reader(f)
    	data = []
    	for i in reader:
    		data.append(i)

    masterlist = []
    for row in data:
        masterlist.append(Movie(row))

    return masterlist


# for movie in masterlist[1:6]:
#     each_movie = movie
#     print(each_movie)
