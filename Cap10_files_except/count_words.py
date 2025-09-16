# %%
from pathlib import Path
# %%
def count_words(path):
    """counts the number of words in a text"""
    
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # return (f'The file {path} does not exist. Check it.')
        pass
    else:
        # counts thw number of words
        words = contents.split()
        num_words = len(words)
        return f'The file {path} has {num_words} words'
# %%
path = Path('alice.txt')
count_words(path)
# %%
books = ['alice.txt','Dracula.txt','judy.txt','Romeo_juliet.txt']
for book in books:
    path = Path(book)
    print(count_words(path))
# %%
