from music import asking_for_songs_per_year as get_songs
from flask import Flask, render_template, request

app = Flask(__name__)

#print(get_songs())

@app.route("/")
def choose_year():
    return render_template("form.html", year="")

@app.route("/top_10_of_the_year", methods=["POST"])
def music_page():
    form = request.form
    year_to_search = form["year"]
    
    return render_template("form.html", year=get_songs(year_to_search)) #this isn't getting anything to website
#if I save  the songs and links to a list, then print that list to a separate template? For example look Day 86 exercise 

app.run(host="0.0.0.0", port=81 )

