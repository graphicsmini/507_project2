import csv

# Open movies_clean.csv file
with open("movies_clean.csv", "r") as f:
	reader = csv.reader(f)
	data = []
	for i in reader:
		data.append(i)


# Define a class Movie that accepts as constructor input one row of the movies_clean.csv file
# class Movie:
#     for i in range(len(data)):
#     	for j in range(len(data[i])):
#             def __init__(self, one_row):
#                 self.one_row = data[i][j]

class Movie:
    def __init__(self, movie_title):
        self.movie_title = data[i][0]
        self.rating = data[i][6]

        self.number = len(data[1:])

    def __str__(self, rating):
        return "{} | {}".format(self.movie_title, self.rating)
