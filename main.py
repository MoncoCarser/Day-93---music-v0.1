from music import print_song
from flask import Flask, request


app = Flask(__name__)

    

@app.route("/")
def choose_year():
    page = ""
    f = open("./templates/form.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{music_printout}", "")
    page = page.replace("{year}", "1988")
    return page


    
    
@app.route("/top_10_of_the_year", methods=["POST"])
def music_page():
    form = request.form
    page = ""
    f = open("./templates/form.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{music_printout}", print_song(form["year"]))
    page = page.replace("{year}", form["year"])
    return page
    

app.run(host="0.0.0.0", port=81 )

