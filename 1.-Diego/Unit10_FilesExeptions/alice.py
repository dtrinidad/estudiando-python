from pathlib import Path

def word_count(path):
    'Function to count words in a text file'
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry but file --{path}-- does not exist")
    else:
        #print the aproximate number of words
        words = contents.split()
        print(f"Your file has {len(words)} words")  

filenames = ["alice.txt", "moby_dick.txt","pi_digits.txt", "ljkj.txt"]
for filename in filenames:
    path = Path(filename)
    word_count(path)