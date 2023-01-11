from music import asking_for_songs_per_year as get_songs
from flask import Flask, render_template, request

app = Flask(__name__)

#print(get_songs())

def print_song(year):
    entry = ""
    f = open("./templates/template.html", "r")
    entry = f.read()
    f.close
    data = get_songs(year)
    content = ""
    for track in data["tracks"]["items"]:
        this_entry = entry
        this_entry = this_entry.replace("{name}", track["name"])
        this_entry = this_entry.replace("{url}", track["preview_url"])
        content += this_entry
    return content
    

@app.route("/")
def choose_year():
    page = ""
    f = open("./templates/form.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{music_printout}", "")
    return page
    
@app.route("/top_10_of_the_year", methods=["POST"])
def music_page():
    form = request.form
    page = ""
    f = open("./templates/form.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{music_printout}", print_song(form["year"]))
    return page
    
    #this isn't getting anything to website
#if I save  the songs and links to a list, then print that list to a separate template? For example look Day 86 exercise 

app.run(host="0.0.0.0", port=81 )

