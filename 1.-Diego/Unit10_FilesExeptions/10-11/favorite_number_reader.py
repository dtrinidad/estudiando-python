from pathlib import Path
import json as js

path = Path("favorite_number.txt")
contents = js.loads(path.read_text())
print(f"I know your favorite number, which is: {contents}")