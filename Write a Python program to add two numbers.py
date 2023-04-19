# Continuously ask the user for a valid input number
while True:
    num1 = input(f'Enter a valid number>\n' + ":")
    if num1.isdigit():
        num1 = int(num1)
        break
    else:
        print('<The number is invalid>')
        
        


while True:
    num2 = input(f'Enter a second valid number>\n' + ":")
    if num2.isdigit():
        num2 = int(num2)
        break
    else:
        print('The number is invalid')
        
     
num3 = num1 + num2  
     
        
print(f'The two sums of the number is {num3}')
        
        
        
     
        
              
        
        
        
        
        
        
        