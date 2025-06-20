from pathlib import Path

path = Path('pi_million_digits.txt')
content = path.read_text()
print(content + "\n")
content_lines = content.splitlines()
print(type(content_lines))

pi_string = '' 
for line in content_lines:
    pi_string += line.lstrip()

print(f"{pi_string[:10]}")
print(len(pi_string))