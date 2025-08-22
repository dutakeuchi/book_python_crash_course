# %%
def greets(list_):
    """greets every user from a list"""
    for user in list_:
        print(f'Hello {user.title()}')
# %%
lista = ['anna','john','ken']
greets(lista)
# %%
def print_models(print_design, finished):
    while print_design:
        design = print_design.pop()
        print(f'Printing {design}')
        finished.append(design)
        
def finished_models(finished):
    print('The following models have been printed')
    for finished_model in finished:
        print(finished_model)
        
print_design = ['case','suport','table','cup']
finished = []

print_models(print_design, finished)
finished_models(finished)
# %%
print(print_design)
print(finished)
# %%
print_design = ['case','suport','table','cup']
finished = []

print_models(print_design[:], finished)
finished_models(finished)
print()
print(print_design)
print(finished)
# %%
