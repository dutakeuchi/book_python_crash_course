# %%
print("Let's sum numbers")

while True:
    num1 = input('Digit any integer number')
    try:
        num1 = int(num1)
        break
    except ValueError:
        print(f'{num1} is invalid')
        
while True:
    num2 = input('Digit any integer number')
    try:
        num2 = int(num2)
        break
    except ValueError:
        print(f'{num2} is invalid')
        
sum_ = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_}")
# %%
5+5
# %%
def get_number():
    while True:
        number = input('Digit any integer number')
        try:
            number = int(number)
            return number
        except ValueError:
            print(f'{number} is invalid')
            
print("Let's sum numbers")

num1 = get_number()
        
num2 = get_number()
        
sum_ = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_}")
# %%
num1
# %%
