from pathlib import Path
import json
location_file = "I_remember.json"
path = Path(location_file)
person_dict = {
    'name': input("What is your name? "),
    'age' : input("What is your age? "),
    'ID'  : input("What is your Id number? ")
}

remember_file = json.dumps(person_dict)
path.write_text(remember_file)
if path.exists():
    user_info = json.loads(path.read_text())
    print(f"Username = {user_info['name']} and the user is {user_info['age']}, its id is {user_info['ID']}")