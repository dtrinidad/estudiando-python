from pathlib import Path

path = Path('numbers.test.json')
path.write_text('[1, 2, 3, 4, 5, 6, 7]')
