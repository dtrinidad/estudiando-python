from pathlib import Path
import json as js

number  = input("Tell me your favorite number: ")
path = Path("favorite_number.txt")
number_store = js.dumps(number)
path.write_text(number_store)

