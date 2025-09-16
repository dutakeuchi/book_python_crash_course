# %%
from pathlib import Path
# %%
path = Path('programming.txt')
path.write_text('I love programming that much')
# %%
contents = 'I love programming'
contents += "I'm learning python"
contents += 'I work with data'
path.write_text(contents)
# %%
contents = 'I love programming\n'
contents += "I'm learning python\n"
contents += 'I work with data\n'
path.write_text(contents)
# %%
text = path.read_text()
for line in text.splitlines():
    print(line)
# %%
contents
# %%
