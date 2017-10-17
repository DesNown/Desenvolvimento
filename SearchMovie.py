from requests import *

req = get("http://www.google.com")
print(req.text)
