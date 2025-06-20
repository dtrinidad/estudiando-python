from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)

path2 = Path('numbers.test.json')
contenido  = path2.read_text()
numbers_test = json.loads(contenido)
print(type(numbers_test))