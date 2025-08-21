# %%
prompt = 'Text anything. Text "quit" to exit'

while True:
    message = input(prompt)
    
    if message == 'quit':
        break
    else:
        print(message)
# %%
prompt = 'Text anything. Text "quit" to exit'

while True:
    message = input(prompt)
    
    if message == 'quit':
        break
        ## this print under here won't be displayed
        print('close')
    else:
        print(message)
# %%
prompt = 'Text anything. Text "quit" to exit'

while True:
    message = input(prompt)
    
    if message == 'quit':
        break

    else:
        print(message)
        print('1')
        print()
    
    message_2 = input(prompt)
    if message_2 == 'quit':
        break

    else:
        print(message_2)
        print('2')
        print()    
# %%
number = input('Digit a number between 1 and 20. I will show all odd numbers and not divide by 3')
number = int(number)
current_number = 0

while current_number < number:
    current_number += 1
    
    if current_number % 2 == 0:
        continue
    
    if current_number % 3 == 0:
        continue
    print(current_number)
# %%
