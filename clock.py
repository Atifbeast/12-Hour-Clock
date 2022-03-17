import time
from tkinter import *

root = Tk()
root.geometry('1400x700')
root.title('CLOCK')
root.config(bg='black')

def watch():
    hour = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    ampm = time.strftime('%p')
    times = f'{hour}:{min}:{sec} {ampm}'
    clock.config(text=times)
    clock.after(1000, watch)

clock = Label(root, text='', fg='cyan', bg='black', font=('comicsansms 160 bold'))
clock.place(x=10, y=160)

watch()
root.mainloop()
