from requests import *

req = get("http://www.omdbapi.com/?t=interstella")
print(req.text)