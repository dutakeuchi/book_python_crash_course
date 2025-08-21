# %%
import time
# %%
sandwich_orders = ['cheese','bacon','egg','chicken','cheese']
sandwich_finished = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    sandwich_finished.append(sandwich)
    print(f'Your {sandwich} sandwich is ready.')
    time.sleep(1)
# %%
sandwich_orders = ['cheese','bacon','egg','chicken','cheese','pastrami','egg',
                   'pastrami','bacon','pastrami']
sandwich_finished = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    if sandwich == 'pastrami':
        print('Sorry, we are out of pastrami')
    else:
        sandwich_finished.append(sandwich)
        print(f'Your {sandwich} sandwich is ready.')
    time.sleep(1)
# %%
sandwich_orders = ['cheese','bacon','egg','chicken','cheese','pastrami','egg',
                   'pastrami','bacon','pastrami']
sandwich_finished = []

while sandwich_orders:
    
    if 'pastrami' in sandwich_orders:
        print('Sorry, we are out of pastrami. Choose another sandwich\n')
        while 'pastrami' in sandwich_orders:
            sandwich_orders.remove('pastrami')
            
    sandwich = sandwich_orders.pop(0)
    sandwich_finished.append(sandwich)
    print(f'Your {sandwich} sandwich is ready.')
    time.sleep(1)
# %%
sandwich_orders = ['cheese','bacon','egg','chicken','cheese','egg','bacon',]
sandwich_finished = []

while sandwich_orders:
    
    if 'pastrami' in sandwich_orders:
        print('Sorry, we are out of pastrami. Choose another sandwich\n')
        while 'pastrami' in sandwich_orders:
            sandwich_orders.remove('pastrami')
            
    sandwich = sandwich_orders.pop(0)
    sandwich_finished.append(sandwich)
    print(f'Your {sandwich} sandwich is ready.')
    time.sleep(1)
# %%
