import urllib2 
import json


def getPlaylist(artist):
    fixedArtist = ""
    if artist.find(" ") != -1:
        for x in xrange(len(artist)):
            if artist[x] == " ":
                fixedArtist += "+"
            else:
                fixedArtist += artist[x]
    else:
        fixedArtist = artist
    #print fixedArtist
    y = urllib2.urlopen("http://developer.echonest.com/api/v4/playlist/static?api_key=KK2PINTHA7KOVR4DK&artist=" + fixedArtist + "&format=json&results=20&type=artist-radio&sort=artist_hotttnesss-desc")
    x = y.read()
    temp = json.loads(x)
    #songDicts = {}
    try:
        return temp["response"]["songs"]
    except KeyError:
        return temp["response"]["status"]
    

def getSongs(aD):
    songs = []
    for diction in aD:
        songs.append(diction["title"])
    return songs 


def getArtists(aD):
    artists = []
    for diction in aD:
        artists.append(diction["artist_name"])
    return artists

def getLinks(aD):
    links = []
    link = "http://songmeanings.com/songs/view/"
    for diction in aD:
        links.append(link + diction["id"] + "/")
    return links

def getInfos(songs, artists, links):
    someList = []
    b = len(songs)
    for x in xrange(b):
        someList.append(songs[x])
        someList.append(artists[x])
        someList.append(links[x])
    return someList

#api key
#KK2PINTHA7KOVR4DK 
