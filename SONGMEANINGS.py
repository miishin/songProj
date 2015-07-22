import urllib2 
import json


def getPlaylist(artist):
    songids = []
    artists = []
    y = urllib2.urlopen("http://developer.echonest.com/api/v4/playlist/static?api_key=KK2PINTHA7KOVR4DK&artist=" + artist + "&format=json&results=20&type=artist-radio&sort=artist_hotttnesss-desc")
    x = y.read()
    temp = json.loads(x)
    songs = temp["response"]["songs"]
    return songs

def getSongs(aD):
    songs = []
    for diction in aD:
        songs.append(diction["title"])
    return songs 


def getIDs(aD):
    songids = []
    for diction in aD:
        songids.append(diction["id"])
    return songids

def getArtists(aD):
    artists = []
    for diction in aD:
        artists.append(diction["artist_name"])
    return artists

def getLinks(aD):
    links = []
    link = "http://http://songmeanings.com/songs/view/"
    for diction in aD:
        links.append(link + diction["id"] + "/")
    return links

def getInfos(songs, artists, links):
    someList = []
    for x in xrange(len(songs)):
        someList.append(songs[x] + "\n" + artists[x] + "\n" + links[x] + "\n")
    return someList

#api key
#KK2PINTHA7KOVR4DK 
