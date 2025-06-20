from pathlib import Path as Pth

my_file_path = Pth('learning_python.txt')

my_file = my_file_path.read_text()
print(my_file)
my_file_lines = my_file.splitlines()
for i in my_file_lines:
    print(i)

for lines in my_file_lines:
    print(lines.replace("Python", "C#"))

