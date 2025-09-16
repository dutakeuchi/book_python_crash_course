# %%
from pathlib import Path
# %%
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)
 # %%
with open('pi_digits.txt', 'r') as file:
    content = file.read()
    lines = content.splitlines()
    print(lines)
# %%
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
lines = contents.splitlines()
pi = ''
for line in lines:
    pi += line
    
pi
# %%
path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()

pi_digits = ''
for line in lines:
    pi_digits += line.lstrip()
        
pi_digits

## getting the first 50 digits
pi_50 = pi_digits[:52]
print(pi_50)
len(pi_50)
# %%
birthday = input('Enter your birthday in the form mmddyy: ')
if birthday in pi_digits:
    print('Your birthday appers in the first millions digits of pi')
else:
    print('Your birthday does not apper in the first millions digits of pi')
# %%
