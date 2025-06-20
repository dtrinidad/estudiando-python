from pathlib import Path as pth
import json as js

path = pth('username.json')
contents =  path.read_text()
username = js.loads(contents)

print(f"Welcome back, {username}")