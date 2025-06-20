from pathlib import Path
import json


path = Path("favorite_number.json")

if path.exists():
    contents = json.loads(path.read_text())
    print(f"I know your favorite number, which is: {contents}")
else:
    number  = input("Tell me your favorite number: ")
    path = Path("favorite_number.json")
    number_store = json.dumps(number)
    path.write_text(number_store)
    