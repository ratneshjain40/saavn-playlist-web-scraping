import json

html_symbols = {
    "&#039;": "\'",
    "&amp;": "&",
    "&quot;": "\""
}

def clean_html_entities(string_list):
    for i,string in enumerate(string_list):
        for key in html_symbols.keys():
            if string.find(key) != -1:
                string_list[i] = string_list[i].replace(key,html_symbols[key])
    return string_list

def song_obj(title,album,artist):
    title, album, artist = clean_html_entities([title,album,artist])
    obj = {
        "title":title,
        "album":album,
        "artist":artist
    }
    return obj

with open('./data_file.json') as f:
  data_file = json.load(f)

playlist_name = data_file["title"]
songs = data_file["list"]
list_count = data_file["list_count"]

songs_list = []
for song in songs:
    title = song["title"]
    album = song["more_info"]["album"]
    artist = song["more_info"]["artistMap"]["primary_artists"][0]["name"]
    songs_list.append(song_obj(title,album,artist))

playlist = {
    "playlist_name":playlist_name,
    "list_count":list_count,
    "list":songs_list
}

with open("jio_playlist.json", "w") as write_file:
    json.dump(playlist, write_file)