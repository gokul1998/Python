import urllib.request
import json
with urllib.request.urlopen("https://googleapis.com/books/v1/volumes?q=isbn:1101904224") as f:
    text = f.read()
    decode = text.decode('utf-8')
    print(decode)