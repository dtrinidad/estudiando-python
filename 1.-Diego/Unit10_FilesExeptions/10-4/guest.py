from pathlib import Path

path = Path('guest.txt')

guest_lists = path.read_text()
guest_lists += input("What is your name? ")
path.write_text(guest_lists + '\n')