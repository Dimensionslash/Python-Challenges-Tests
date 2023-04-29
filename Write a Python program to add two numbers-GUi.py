import tkinter as tk


def calculate_sum():
    try:
        num1 = int(num1_entry.get())
        num2 = int(num2_entry.get())
        num3 = num1 + num2
        result_label.config(text=f"The sum of {num1} and {num2} is {num3}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")


# Create the main window
root = tk.Tk()
root.title("Number Sum Calculator")

# Create the number input fields and labels
num1_label = tk.Label(root, text="Enter a valid number:")
num1_entry = tk.Entry(root)
num2_label = tk.Label(root, text="Enter a second valid number:")
num2_entry = tk.Entry(root)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_sum)

# Create the result label
result_label = tk.Label(root, text="")

# Add the widgets to the window
num1_label.pack()
num1_entry.pack()
num2_label.pack()
num2_entry.pack()
calculate_button.pack()
result_label.pack()

# Start the main event loop
root.mainloop()
