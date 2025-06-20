from pathlib import Path
import json as js

path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = js.loads(contents)
    print(f"Welcome back, {username}")
else:
    username = input("What is your name? ")
    contents = js.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}")