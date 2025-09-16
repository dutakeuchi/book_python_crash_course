# %%
from pathlib import Path
import json
# %%
while True:
    fav_number = input('Digit your favorite number')
    try:
        fav_number = int(fav_number)
        break
    except ValueError:
        print('Digit a valid number')
        
path = Path('favorite_number.json')
contents = json.dumps(fav_number)
path.write_text(contents)
# %%
path = Path('favorite_number.json')
contents = path.read_text()
json.loads(contents)
# %%
path = Path('favorite_number.json')
if path.exists():
    contents = path.read_text()
    fav_number = json.loads(contents)
    print(f'Your favorite number is {fav_number}')
    
else:
    while True:
        fav_number = input('Digit your favorite number')
        try:
            fav_number = int(fav_number)
            break
        except ValueError:
            print('Digit a valid number')
            
    path = Path('favorite_number.json')
    contents = json.dumps(fav_number)
    path.write_text(contents)
    print('Your favorite number is saved. We will remember next time')
# %%
def get_stored_number(path):
    if path.exists():
        contents = path.read_text()
        fav_number = json.loads(contents)
        return fav_number
    
    else:
        return None
    
def get_favorite_number_first():
    while True:
        fav_number = input('Digit your favorite number')
        try:
            fav_number = int(fav_number)
            break
        except ValueError:
            print('Digit a valid number')
                
    path = Path('favorite_number.json')
    contents = json.dumps(fav_number)
    path.write_text(contents)
    print('Your favorite number is saved. We will remember next time')

    
def get_favorite_number():
    path = Path('favorite_number.json')
    fav_number = get_stored_number(path)
    
    if fav_number:
        return (f'Your favorite number is {fav_number}')
        
    else:
        get_favorite_number_first()
# %%
get_favorite_number()
# %%
