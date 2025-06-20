from pathlib import Path

my_file = Path('pi_million_digits.txt').read_text().splitlines()
my_birth_date = "87849491"
my_file_string = ''
for lines in my_file:
    my_file_string += lines.lstrip()

for position in range(2, len(my_file_string)):
    compare_position = my_file_string[int(position):int(position)+8]
    if my_birth_date == compare_position:
        print(f" - - - my birth date in pi is located at {position} - - -")