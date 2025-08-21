# %%
prompt = 'Text anything here. Text "quit" to exit.'
flag = True

while flag:
    message = input(prompt)
    
    if message != 'quit':
        print(message)
    elif message == 'quit':
        flag = False
# %%
prompt = 'Text anything here. Text "quit" to exit.'
flag = True

while flag:
    message = input(prompt)
    
    if message != 'quit':
        print(message)
        print('The program keep going')
    elif message == 'quit':
        flag = False
        print('Closing program')
        
# %%
prompt = 'Text anything here. Text "quit" to exit.'
flag = True

while flag:
    message = input(prompt)
    
    if message != 'quit':
        print(message)
        print('The program keep going')
    elif message == 'quit':
        flag = False
        print('Closing program')
        
    message_2 = input(prompt)
    
    if message_2 != 'quit':
        print(message_2)
        print('continue')
    elif message_2 == 'quit':
        flag = False
        print('Close')
        
## this doesn't work well. It goes to message_2 even though message is 'quit'
# %%
prompt = 'Text anything here. Text "quit" to exit.'
flag = True

while flag:
    message = input(prompt)
    
    if message != 'quit':
        print(message)
        print('The program keep going')
        
        message_2 = input(prompt)
        
        if message_2 != 'quit':
            print(message_2)
            print('continue')
        elif message_2 == 'quit':
            flag = False
            print('Close')
        
    elif message == 'quit':
        flag = False
        print('Closing program')
        
# %%
