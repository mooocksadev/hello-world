import tkinter as tk
from time import strftime

# define time function
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Create a tkinter window
root = tk.Tk()
root.title('Digital Clock')

# Create a label
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Call the time function
time()

# Set the window size
root.geometry('400x150')
root.configure(bg='black')

# Run the loop
root.mainloop()
