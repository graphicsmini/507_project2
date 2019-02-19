# About this program

As you can see in requirements.txt file, you need to install flask. to run this whole program.
You will see two python files, which is 'SI507_project2.py' and 'movies_tools.py'. The file 'movies_tools.py' is essential source code for running 'SI507_project2.py' file.

### WHAT 'movies_tools.py' CONTAINS
1. It has class named **Movie** which brings movie title, and movie rating.
2. Also, class Movie has string method that shows title, and rating of the movie. 
3. It has function named **process**. This opens csv file, read, and put the each row into the list.


### WHAT 'SI507_project2.py' CONTAINS
1. It has **flask** application which allow uers to go to the routes at the following paths.
2. There are total two routes.
  - http://localhost:5000/
    - *You will see "3146 movies recorded."*
  - http://localhost:5000/movies/ratings/
    - *You will see*
    > * The Land Girls | 6.1
    > * First Love, Last Rites | 6.9
    > * I Married a Strange Person | 6.8
    > * Let's Talk About Sex | NA
    > * Slam | 3.4
    > * Mississippi Mermaid | NA


### HOW TO RUN (IN LOCAL COMPUTER)
* Open terminal or any command prompt you have.
* Make sure you have installed all in **requirements.txt** like flask.
* Type: python SI507_project2.py
* Then, open Chrome or Safari and go to http://localhost:5000/
    *You will see '3146 movies recorded.' in the window.*
