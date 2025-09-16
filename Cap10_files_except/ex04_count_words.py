# %%
from pathlib import Path
# %%
path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f'File {path} does not exist')
    

alice_count = contents.lower().count("alice")
alice_count
# %%
