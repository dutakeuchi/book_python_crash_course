# %%
from pathlib import Path
# %%
contents = Path('learning_python.txt')
contents = contents.read_text()

for line in contents.splitlines():
    print(line)
print()
print(contents)
# %%
guest = Path('guest_name.txt')

names = ''
while True:
    name = input("What is your name? Digit quit to stop")
    if name.lower() == 'quit':
        break
    else:
        names += f'{name.title()}\n'
        
guest.write_text(names)
text = guest.read_text()
for line in text.splitlines():
    print(line)
# %%
