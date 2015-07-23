from flask import Flask, render_template, request
import SONGMEANINGS as song

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("basic.html", info = "http://www.google.com")


@app.route("/song", methods = ["POST"])
def songPage ():
    check = True 
    x = request.form["artistName"]
    playlist = song.getPlaylist(x)
    #print "playlist made"
    try:
        songs = song.getSongs(playlist)
        artists = song.getArtists(playlist)
        links = song.getLinks(playlist)
    except KeyError:
        songs = ["Error"]
        artists = ["Song Not"]
        links = ["Found"]
    infos = song.getInfos(songs, artists, links)
    #print "all set up"
    nums = [0, 3, 6, 9, 12, 15, 18, 21]
    return render_template("basic.html", nums = nums,info = infos)

if __name__ == "__main__":
    app.run()
