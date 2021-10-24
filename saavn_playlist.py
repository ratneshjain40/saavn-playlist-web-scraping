import requests
import json

def parse_url(url):
    token = url.split("/")[-1:]
    print(token)
    return token

def get_api(token,song_limit = 300):
    api = f'https://www.jiosaavn.com/api.php?__call=webapi.get&token={token}&type=playlist&p=1&n={song_limit}&includeMetaTags=0&ctx=web6dot0&api_version=4&_format=json&_marker=0'
    return api

url = f'<Replace Your Playlist URL HERE>'
token = parse_url(url)

# pass a second parameter if your playlist size is greater than 300
api = get_api(token)

s = requests.session()
res = s.get(url)
api_response = s.get(api)
data = api_response.json()

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)