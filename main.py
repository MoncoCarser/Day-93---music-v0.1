from music import asking_for_songs_per_year as get_songs
from flask import Flask, render_template

app = Flask(__name__)

#print(get_songs())

@app.route("/")
def music_page():
    return render_template("form.html")

app.run(host="0.0.0.0", port=81 )