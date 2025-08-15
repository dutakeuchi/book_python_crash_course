# %%
numbers = [number for number in range(1,21)]
numbers
# %%
for number in range(1,1001):
    print(number)
# %%
numbers = [number for number in range(1,1000001)]
print(f'Minimum: {min(numbers)}')
print(f'Maximum: {max(numbers)}')
print(f'Sum: {sum(numbers)}')
# %%
for number in range(1,21,2):
    print(number)
# %%
for number in range(3,31,3):
    print(number)
# %%
for number in range(1,11):
    cube = number ** 3
    print(f'{number}^3: {cube}')
# %%
cube = [number**3 for number in range(1,11)]
cube
# %%
