

# (App to convert lbs to grams)

from tkinter import*
from tkinter import ttk
import os
import sys

root = Tk()
root.configure(bg = 'gray20')
root.geometry('250x290')
root.title('Converter')

#def sweep():
	

def stop():
    sys.exit()
   

var = DoubleVar()
'''
def rec_conversion():
    x = eval(e1.get())
    z = x * float(453.59237)
    #print (type(z))
    var.set(z)
    print(z)
    
    #l5 = Text(root, text = (var), font = 'Arial 10',width = 10, fg = 'black', bg = 'white' )
    #l5.pack(pady = 20)
'''
def rec_conversion():
    x = eval(e1.get())
    z = x * float(453.59237)
    #print (type(z))
    var.set(z)
    #print(z)
    l7.destroy()
    l5 = Label(root,textvar = var ,font = 'Arial 10',width = 18, fg = 'black', bg = 'gray90' )
    l5.pack(pady = 10)
  

# ------------------  print ("(--- Pounds to Grams Coverter ---)")

l1 = Label(root, text = 'Pounds To Grams Converter', font = 'Times 12 italic', fg = 'white', bg = 'gray20' )
l1.pack(pady = 20)

l2 = Label(root, text = 'Enter number in pounds',font = 'Arial 10',fg = 'gray88', bg = 'gray20' )
l2.pack(pady = 10)
#a = eval(input("Enter number in lbs: " ))

'''
e1 = Entry(root, width = 6,fg = 'black', relief = SOLID, bg = 'gray90', justify = CENTER)
e1.focus()
e1.pack(pady = 15)
'''
e1= ttk.Entry(root, justify = CENTER, width = 6)
e1.focus()
e1.pack()


b1 = Button(root, text = 'Convert',font = 'Arial 9 italic', width = 6, bg = 'gray90',command = rec_conversion )
b1.pack(pady = 10)


l7 = Label(root, font = 'Arial 10',width = 18, fg = 'gray88', bg = 'gray90' )
l7.pack(pady = 10)

#l12 = Label(root, text = 'grams')
#l12.pack( pady = (0,600))

#b2 = Button(root, text = 'Get Result', font = 'Arial 10 italic ', width = 10, bg = 'gray90')
#b2.pack(pady = 20)


b9 = Button(root, text = 'Quit',font = 'Arial 9 italic', command = stop)
b9.pack( side = BOTTOM,pady = 15)

# ------------------  print (type(a))

# ------------------  print (isinstance(a, (int, float)))





root.mainloop()



