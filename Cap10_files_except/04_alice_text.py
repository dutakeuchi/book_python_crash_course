# %%
from pathlib import Path
# %%
path = Path('Dracula.txt')
try:
    contents = path.read_text(encoding='utf-8')
except UnicodeDecodeError:
    print('encoding problem')
except FileNotFoundError:
    print('File problem')
except:
    print('Problem, contact admin')
# %%
len(contents.split())
# %%
path
# %%
contents
# %%
