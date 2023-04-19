print('Hello world') 
import tkinter as tk

def submit_order():
    name = name_entry.get()
    menu = menu_var.get()
    cube_sugar = sugar_entry.get()

    # Check if the sugar input is a valid number
    if not cube_sugar.isdigit():
        status_label.config(text="Invalid input. Please enter a valid number.")
        return

    cube_sugar = int(cube_sugar)
    status_label.config(text=f"Thanks, {name}! Your order of {menu} will be ready shortly and will have {cube_sugar} sugar cubes. Thank you!")

# Create the main window
root = tk.Tk()
root.title("Lulu's Coffee Shop")

# Create the widgets
welcome_label = tk.Label(root, text="Welcome to Lulu's Coffee Shop")
name_label = tk.Label(root, text="What is your name?")
name_entry = tk.Entry(root)
menu_label = tk.Label(root, text="What would you like from the menu?")
menu_var = tk.StringVar()
menu_options = ["Coffee", "Latte", "Cappuccino", "Americano", "Espresso", "Iced Coffee"]
menu_dropdown = tk.OptionMenu(root, menu_var, *menu_options)
sugar_label = tk.Label(root, text="How many cubes of sugar would you like in your coffee?")
sugar_entry = tk.Entry(root)
submit_button = tk.Button(root, text="Submit", command=submit_order)
status_label = tk.Label(root, text="")

# Add the widgets to the window
welcome_label.pack()
name_label.pack()
name_entry.pack()
menu_label.pack()
menu_dropdown.pack()
sugar_label.pack()
sugar_entry.pack()
submit_button.pack()
status_label.pack()

# Run the main loop
root.mainloop()
