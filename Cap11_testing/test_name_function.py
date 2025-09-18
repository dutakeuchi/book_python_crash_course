# %%
from name_function import get_formatted_name
# %%
def test_first_last_name():
    '''testing our function name_function'''
    formatted_name = get_formatted_name('john','obama')
    assert formatted_name == 'John Obama'
    
# %%
def test_first_middle_last_name():
    '''testing our function name_function'''
    formatted_name = get_formatted_name('john','obama', 'carlos')
    assert formatted_name == 'John Carlos Obama'