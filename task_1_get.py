"""
api keys - 

"""

import requests

url = "https://www.flickr.com/services/rest/"

parametrs = {
    "method":"flickr.photos.getPopular",
    "api_key":"01c92a9b2bb5021ac63952dc3d3ffb7b", #my personal api keys
    "user_id":"195809336@N04", #user id
    "format":"json",
    "nojsoncallback":1
}

r = requests.get(url=url, params=parametrs)

print(r.status_code)
json_response = r.json()
print(json_response)


if (r.status_code == 200 and json_response["stat"] == "ok" ):
    print("API Working")
else:
    print("Not Working")
    print("Error caught :-",json_response["message"])