from tkinter import *
import sys


root = Tk()
root.geometry('300x410')
root.config(bg = 'black')
root.title("Process Solutions")


def kill():
    t1 = Label(root, bg = 'black',fg = 'black', height = 12, text = '1. Is the material dry? \n 2. Are all heats working correctly? \n 3. Do you need as much decompression?')
    t1.grid(row = 4, column = 1, padx = 10)

    


def stop():
    sys.exit()

def get_info():
    textvar2 = StringVar()
    textvar2 = var.get()
    
    if textvar2 == 'Flash':
        sol.flash()
    
    if textvar2 == 'Splay':
        
        sol.splay()
         
    
    if textvar2 == 'Short':
        sol.short()
    
    if textvar2 == 'Warp':
        sol.warp()
    
    if textvar2 == 'Swirl':
        sol.swirl()
    
    if textvar2 == 'Pin Push':
        sol.pin_push() 
    


class Solutions:
    
    

    def flash(self):
        t2 = Label(root, text = ' 1. Is the tonnage set correctly? \n 2. Anything stuck in the mold? \n 3. Are all water valves on?', bg = 'black', fg = 'white')
        t2.config(justify = LEFT)
        t2.grid(row = 4, column = 1, padx = 20) 



    def splay(self):        
        t2 = Label(root, text = ' 1. Is the material dry? \n 2. Are all heats working correctly? \n 3. Do you need as much decomp.?', bg = 'black', fg = 'white')
        t2.config(justify = LEFT)
        t2.grid(row = 4, column = 1, padx = 20) 
 

    def short(self):
        t2 = Label(root, text = ' 1. Make sure nozzle is not leaking. \n 2. Are all heats working correctly? \n 3. Increase fill speed. \n 4. May have to lower transfer position.', bg = 'black', fg = 'white')
        t2.config(justify = LEFT)
        t2.grid(row = 4, column = 1, padx = 20) 
   

    def warp(self):
        t2 = Label(root, text = ' 1. Mold watered correctly? \n 2. Do you have enough cooling? \n 3. Is hold and time set correctly?', bg = 'black', fg = 'white')
        t2.config(justify = LEFT)
        t2.grid(row = 4, column = 1, padx = 20) 
 

    def swirl(self):
        t2 = Label(root, text = ' 1. Is  conc.loader setup correctly? \n 2. Raise BP to mix better. \n 3. Raise heats in the back of barrel. \n 4. Run with a bigger cushion.', bg = 'black', fg = 'white')
        t2.config(justify = LEFT)
        t2.grid(row = 4, column = 1, padx = 20) 


    def pin_push(self):
        t2 = Label(root, text = ' 1. Check thermolators. \n 2. Heats working correctly? \n 3. Cooling time set correctly? \n 4. Slow ejection down.', bg = 'black', fg = 'white')
        t2.config(justify = LEFT)
        t2.grid(row = 4, column = 1, padx = 20) 
 



sol = Solutions()  
var = StringVar()
textvar2 = StringVar()


l1 = Label(root, text = "Process Tech Help Guide",font = 'Times 15 italic ', bg = 'black', fg = 'white')
l1.config(justify = CENTER)
l1.grid(row = 0, column = 1, pady = 8)

choices = { 'Flash','Splay','Short','Warp','Swirl','Pin Push'}
var.set('Issues') # set the default option
popupMenu = OptionMenu(root, var, *choices)


Label(root, text="Pick an issue below \n then press enter", font = 'Arial 12 ', bg = 'black', fg = 'white').grid(row = 1, column = 1, pady = 2)
popupMenu.grid(row = 2, column = 1, pady = 5 )

b2 = Button(root, text = 'Enter', command = get_info)
b2.grid(row = 3 , column = 1, pady = 5 )



t1 = Label(root, bg = 'black',fg = 'black', height = 12, text = '1. Is the material dry? \n 2. Are all heats working correctly? \n 3. Do you need as much decompression?')
t1.grid(row = 4, column = 1, padx = 10)

l8 = Label(root, text = 'Press reset to choose again', font = 'Arial 12 ',bg = 'black', fg = 'white')
l8.grid(row = 5, column = 1)

b9 = Button(root, text = 'Reset', command = kill)
b9.grid(row = 6, column = 1, pady = 40)

b5 = Button(root, text = 'Quit', command = stop )
b5.grid(row = 7, column = 1, pady = 20)




root.mainloop()