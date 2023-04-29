import tkinter as tk
import time


class HealthApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Health Game")
        self.health = 100.0
        self.health_canvas = tk.Canvas(
            master, width=300, height=50, bg='white')
        self.health_canvas.pack(side=tk.TOP, padx=10, pady=10)
        self.health_bar = self.health_canvas.create_rectangle(
            0, 0, self.health*3, 50, fill='green')
        self.health_label = tk.Label(
            master, text=f"Health: {self.health:.1f}", font=('Arial', 14, 'bold'))
        self.health_label.pack(side=tk.TOP, padx=10, pady=10)
        self.health_frame = tk.Frame(master)
        self.health_frame.pack(side=tk.TOP, padx=10, pady=10)

        self.inc_button = tk.Button(self.health_frame, text="Increase", command=self.increase_health, font=(
            'Arial', 14, 'bold'), bg='green', fg='white')
        self.inc_button.pack(side=tk.LEFT, padx=10)

        self.dec_button = tk.Button(self.health_frame, text="Decrease", command=self.decrease_health, font=(
            'Arial', 14, 'bold'), bg='red', fg='white')
        self.dec_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.health_frame, text="Reset", command=self.reset_health, font=(
            'Arial', 14, 'bold'), bg='blue', fg='white')
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.increasing = False

    def increase_health(self):
        self.health *= 1.01
        self.health = min(self.health, 100.0)
        self.health_canvas.itemconfig(self.health_bar, width=self.health*3)
        self.health_label.config(text=f"Health: {self.health:.1f}")
        if self.health == 100.0 and self.increasing:
            self.increasing = False

    def decrease_health(self):
        self.health *= 0.99
        self.health_canvas.itemconfig(self.health_bar, width=self.health*3)
        self.health_label.config(text=f"Health: {self.health:.1f}")

    def reset_health(self):
        self.health = 0.0
        self.health_canvas.itemconfig(self.health_bar, width=self.health*3)
        self.health_label.config(text=f"Health: {self.health:.1f}")
        if not self.increasing:
            self.increasing = True
            self.start_increasing()

    def start_increasing(self):
        if self.health < 100.0:
            self.health += 1.0
            self.health = min(self.health, 100.0)
            self.health_canvas.itemconfig(self.health_bar, width=self.health*3)
            self.health_label.config(text=f"Health: {self.health:.1f}")
            self.master.after(1000, self.start_increasing)


root = tk.Tk()
root.geometry("400x200")
root.config(bg='white')
app = HealthApp(root)
root.mainloop()
