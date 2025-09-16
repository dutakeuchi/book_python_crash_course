# %%
5/0
# %%
try:
    5/0
except:
    print('You can not divide by zero')
# %%
print("Let's divide 2 numbers")
print("Press 'q' to exit")

while True:
    first_number = input('Digit the first number')
    if first_number == 'q':
        break
    second_number = input('Digit the second number. It can not be zero')
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print('You can not divide by zero')
    else:
        print(answer)
# %%
print("Let's divide 2 numbers")
print("Press 'q' to exit")

while True:
    first_number = input('Digit the first number')
    if first_number == 'q':
        break
    second_number = input('Digit the second number. It can not be zero')
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number)/int(second_number)
    except:
        # this create a generic error
        print('An unexpected error occurred!')
    else:
        print(answer)
# %%
print("Let's divide 2 numbers")
print("Press 'q' to exit")

while True:
    first_number = input('Digit the first number')
    if first_number == 'q':
        break
    second_number = input('Digit the second number. It can not be zero')
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print('You can not divide by zero')
    except ValueError:
        print('error')
    else:
        print(answer)
# %%
from pathlib import Path
path = Path('alice.txt')
contents = path.read_text()
# %%
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text()
except FileNotFoundError:
    print(f'{path} do not exist')
# %%
