name = input('Please insert your name: ')
# age = int(input('please inset your age: '))
age = int(input(f'Hello {name} could you please type your age: '))
age_res = 18
if age>age_res:
    print('your ID will printed')
elif age<age_res:
    print(f'please come back in a {age_res-age} years')