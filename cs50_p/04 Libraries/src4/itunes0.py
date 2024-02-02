import json 
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1]
)
# print(json.dumps(response.json(), indent=4))

o = response.json()
for result in o["results"]:
    print(result["trackName"], result["artistName"], result["collectionName"])