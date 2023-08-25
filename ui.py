import tkinter as tk
import tkinter.ttk
from tkinter import font


root = tk.Tk()
root.title("2048")

grid = [[0] * 4 for _ in range(4)]

my_frame = tk.Frame(root)
my_frame.pack(pady=10)

fontObj = font.Font(size=28)


labels = [[None for y in range(4)]for x in range(4)]
for x in range(4):
    for y in range(4):
        lb = tk.Label(my_frame, text=grid[y][x], padx=10, pady=10, font=fontObj)
        labels[y][x] = lb
        lb.grid(row=y+1, column=x+1)

# Create left Button
left_button = tk.Button(my_frame, text="Left", font=("Helvetica", 24))
left_button.grid(row=1, rowspan=4, column=0)

# Create right Button
right_button = tk.Button(my_frame, text="Right", font=("Helvetica", 24))
right_button.grid(row=1, rowspan=4, column=5)

# Create up Button
up_button = tk.Button(my_frame, text="Up", font=("Helvetica", 24))
up_button.grid(row=0, columnspan=4, column=1)

# Create down Button
down_button = tk.Button(my_frame, text="Down", font=("Helvetica", 24))
down_button.grid(row=5, columnspan=4, column=1)

sep = tkinter.ttk.Separator(my_frame)

tkinter.ttk.Separator(my_frame, orient=tk.VERTICAL).grid(column=0, row=1, rowspan=4, sticky='nse')
tkinter.ttk.Separator(my_frame, orient=tk.VERTICAL).grid(column=4, row=1, rowspan=4, sticky='nse')
tkinter.ttk.Separator(my_frame, orient=tk.HORIZONTAL).grid(column=1, row=0, columnspan=4, sticky='ews')
tkinter.ttk.Separator(my_frame, orient=tk.HORIZONTAL).grid(column=1, row=4, columnspan=4, sticky='wes')

quit_button = tk.Button(master=root, text="Quit", command=root.destroy)
quit_button.pack()
