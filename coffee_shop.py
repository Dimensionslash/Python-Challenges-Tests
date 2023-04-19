print("Welcome to Lulus Coffee Shop\n")

name = input('Your name please?\n' + ":")


print("Menu items:\n")
print("- Coffee")
print("- Latte")
print("- Cappuccino")
print("- Americano")
print("- Espresso")
print("- Iced Coffee\n")

menu = input("What would you like from the menu?\n" + ":")



while True:
    cube_sugar = input("How many cubes of sugar would you like in your coffee?\n" + ":")
    if cube_sugar.isdigit():
        cube_sugar = int(cube_sugar)
        break
    else:
        print("Invalid input. Please enter a valid number.")

print(f"Thanks, {name}! Your order of {menu} will be ready shortly and will have {str(cube_sugar)} sugar cubes. Thank you!")
        
               
        
        
        
        
        
        
        
        




