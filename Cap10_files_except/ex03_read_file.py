# %%
from pathlib import Path
# %%
path = Path('ex03_cats.txt')
try:
    contents = path.read_text()
except FileNotFoundError:
    print(f'The file {path} does not exist')
    
for name in contents.split():
    print(name)
# %%
