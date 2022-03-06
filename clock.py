
import sys
from tkinter import*
import time

def tick():
	time_string = time.strftime("%H:%M:%S")
	clock.config(text = time_string)
	clock.after(200,tick)
	
def stop():
	quit()
	
root = Tk()
root.config(bg = 'black')


f1 = Frame(root, bg = 'black')
f1.grid(row = 0, column = 1)

clock = Label(f1,font = ('Times',30,'italic'),bg = 'black',fg = 'white',bd = 12,relief = RAISED)
clock.grid(row = 0, column = 1,pady = 200,padx = 100)

b1 = Button(root,text = 'Quit',bg = 'black', fg = 'white',bd = 5, relief = RAISED,command = stop)
b1.grid(row = 2,column = 1,pady = 490)


tick()
root.mainloop()