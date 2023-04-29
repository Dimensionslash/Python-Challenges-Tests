# Write a Python program that asks the user for their age and then prints a message indicating whether they are a child (age 12 or below), a teenager (age 13-17), or an adult (age 18 or above).

age = int(input('What is your age?\n' + ': '))

# '''This statement says if you are greater than 12 and greater than 17 you are an adult if you are not greater than 17 you are a teenager  if you are not greater than 12 you are a child'''

if age <= 12:
    print('You are a child')
elif age <= 17:
    print('You are a teenager')
else:
    print('You are an adult')       
    
    
    
