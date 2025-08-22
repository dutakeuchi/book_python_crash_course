# %%
def make_shirt(size, message):
    print(f'Your shirt will be {size.upper()} size and written {message}')
    
make_shirt('m','Python')
make_shirt(message = 'Java', size = 'pp')
# %%
def make_shirt(message, size='L'):
    """function to get shirt size and message"""
    print(f'Your shirt will be {size.upper()} size and written {message}')
    
make_shirt('Python')
make_shirt("Ruby", size='m')
# %%
