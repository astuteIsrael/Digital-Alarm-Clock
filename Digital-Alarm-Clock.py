import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")


def time():
    string = strftime('%H:%M:%S %P \n %D')
    label.config(text=string)
    label.after(1000,time)

label = tk.Label(root, font=('calibri', 55, 'bold'), background='grey', foreground='black')
label.pack(anchor='center')

time()

root.mainloop