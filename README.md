# About this program

As you can see in requirements.txt file, you need to install flask. to run this whole program.
You will see two python files, which is 'SI507_project2.py' and 'movies_tools.py'. The file 'movies_tools.py' is essential source code for running 'SI507_project2.py' file.

###[WHAT 'movies_tools.py' CONTAINS]
1. It has class named **Movie** which brings movie title, and movie rating.
2. Also, class Movie has string method that shows title, and rating of the movie. 
3. It has function named **process**. This opens csv file, read, and put the each row into the list.


###[WHAT 'SI507_project2.py' CONTAINS]
1. It has **flask** application which allow uers to go to the routes at the following paths.
2. There are total two routes.
  - http://localhost:5000/
    *You will see "3146 movies recorded."*
  - http://localhost:5000/movies/ratings/
    *You will see*
    >The Land Girls | 6.1
    >First Love, Last Rites | 6.9
    >I Married a Strange Person | 6.8
    >Let's Talk About Sex | NA
    >Slam | 3.4
    >Mississippi Mermaid | NA

###[HOW TO RUN]
1. Open terminal or any command prompt you have.
To run this program in the virtual environment, first of all, we are going to make and activate the virtual environment.
2. Type: python3 -m venv project1-env
3. Type: source project1-env/bin/activate
4. Type: pip install -r requirements.txt

Since 'requirements.txt' contains Flask, now you will have flask app in your virtual environment.
To run 'SI507_project2.py' file,
5. Type: python SI507_project2.py runserver
6. Then, open Chrome or Safari and go to http://localhost:5000/
    *You will see 'Welcome to the banking application!' in the window.*
