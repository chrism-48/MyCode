
from tkinter import*
import random

root = Tk()
root.config(bg = 'black')

class Game:
    
    def place_x_b1(self):               
        if self.pick_player == 1:           
            self.b1.destroy()
            textvar = 'X'     
            self.b1 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)            
            self.b1.grid(row = 1, column = 0,padx = 20,pady = 20)

            
        if self.pick_player == 2:                     
            self.b1.destroy()
            textvar = 'O'      
            self.b1 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)          
            self.b1.grid(row = 1, column = 0,padx = 20,pady = 20)
        self.winner()
           

    def place_x_b2(self):              
        if self.pick_player == 1:           
            self.b2.destroy()
            textvar = 'X'                
            self.b2 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)            
            self.b2.grid(row = 1, column = 1,padx = 20,pady =20)
            
        if self.pick_player == 2:           
            self.b2.destroy()
            textvar = 'O'                
            self.b2 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)            
            self.b2.grid(row = 1, column = 1,padx = 20,pady =20)
        self.winner()
            

    def place_x_b3(self):               
        if self.pick_player == 1:           
            self.b3.destroy()
            textvar = 'X'              
            self.b3 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)            
            self.b3.grid(row = 1, column = 2,padx = 20,pady = 20)
            
        if self.pick_player == 2:           
            self.b3.destroy()
            textvar = 'O'              
            self.b3 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)
            
            self.b3.grid(row = 1, column = 2,padx = 20,pady = 20)
        self.winner()
              

    def place_x_b4(self):              
        if self.pick_player == 1:           
            self.b4.destroy()
            textvar = 'X'                 
            self.b4 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3, width = 3)            
            self.b4.grid(row = 2, column = 0,pady = 20)
            
        if self.pick_player == 2:           
            self.b4.destroy()
            textvar = 'O'                 
            self.b4 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3, width = 3)
          
            self.b4.grid(row = 2, column = 0,pady = 20)
        self.winner()
             

    def place_x_b5(self):                
        if self.pick_player == 1:           
            self.b5.destroy()
            textvar = 'X'                 
            self.b5 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3, width = 3)            
            self.b5.grid(row = 2, column = 1,pady = 20)
            

        if self.pick_player == 2:           
            self.b5.destroy()
            textvar = 'O'                 
            self.b5 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3, width = 3)           
            self.b5.grid(row = 2, column = 1,pady = 20)
        self.winner()
              
    def place_x_b6(self):              
        if self.pick_player == 1:           
            self.b6.destroy()
            textvar = 'X'               
            self.b6 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)            
            self.b6.grid(row = 2, column = 2,pady = 20)
            
        if self.pick_player == 2:           
            self.b6.destroy()
            textvar = 'O'               
            self.b6 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)            
            self.b6.grid(row = 2, column = 2,pady = 20)
        self.winner()
              

    def place_x_b7(self):             
        if self.pick_player == 1:           
            self.b7.destroy()
            textvar = 'X'                
            self.b7 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)            
            self.b7.grid(row = 3, column = 0,pady = 20)
            

        if self.pick_player == 2:                
            self.b7.destroy()
            textvar = 'O'                
            self.b7 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)          
            self.b7.grid(row = 3, column = 0,pady = 20)
        self.winner()
                
    def place_x_b8(self):              
        if self.pick_player == 1:           
            self.b8.destroy()
            textvar = 'X'               
            self.b8 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)          
            self.b8.grid(row = 3, column = 1,pady = 20)
            

        if self.pick_player == 2:           
            self.b8.destroy()
            textvar = 'O'               
            self.b8 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)            
            self.b8.grid(row = 3, column = 1,pady = 20)
        self.winner()
            
    def place_x_b9(self):               
        if self.pick_player == 1:           
            self.b9.destroy()
            textvar = 'X'                 
            self.b9 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3, width = 3)           
            self.b9.grid(row = 3, column = 2,pady = 20)
            
        if self.pick_player == 2:           
            self.b9.destroy()
            textvar = 'O'                 
            self.b9 = Button(self.f1, text = textvar,font = ('Arial',9,'bold'),bg = 'white',height = 3, width = 3)           
            self.b9.grid(row = 3, column = 2,pady = 20)
        self.winner()
            


    def new(self):
        
                 
        self.b1 = Button(self.f1, text = " ",bg = 'white',        height = 3,width = 3,command = self.place_x_b1)
        self.b1.bind("<Button-1>",self.btn_click1)
        self.b1.grid(row = 1, column = 0,padx = 20,  pady = 20)

        self.b2 = Button(self.f1, text = " ",bg = 'white',        height = 3,width = 3,command = self.place_x_b2)
        self.b2.bind("<Button-1>",self.btn_click1)
        self.b2.grid(row = 1, column = 1,padx = 20,  pady =20)

        self.b3 = Button(self.f1, text = " ",bg = 'white',        height = 3,width = 3,command = self.place_x_b3)
        self.b3.bind("<Button-1>",self.btn_click1)
        self.b3.grid(row = 1, column = 2,padx = 20,  pady = 20)

        self.b4 = Button(self.f1, text = " ",bg = 'white',        height = 3,width = 3,command = self.place_x_b4)
        self.b4.bind("<Button-1>",self.btn_click1)
        self.b4.grid(row = 2, column = 0,pady = 20)

        self.b5 = Button(self.f1, text = " ",bg = 'white',        height = 3,width = 3,command = self.place_x_b5)
        self.b5.bind("<Button-1>",self.btn_click1)
        self.b5.grid(row = 2, column = 1,pady = 20)

        self.b6 = Button(self.f1, text = " ",bg = 'white',        height = 3,width = 3,command = self.place_x_b6)
        self.b6.bind("<Button-1>",self.btn_click1)
        self.b6.grid(row = 2, column = 2,pady = 20)

        self.b7 = Button(self.f1, text = " ",bg = 'white',        height = 3,width = 3,command = self.place_x_b7)
        self.b7.bind("<Button-1>",self.btn_click1)
        self.b7.grid(row = 3, column = 0,pady = 20)

        self.b8 = Button(self.f1, text = " ",bg = 'white',        height = 3,width = 3,command = self.place_x_b8)
        self.b8.bind("<Button-1>",self.btn_click1)
        self.b8.grid(row = 3, column = 1,pady = 20)

        self.b9 = Button(self.f1, text = " ",bg = 'white',        height = 3, width = 3,command = self.place_x_b9)
        self.b9.bind("<Button-1>",self.btn_click1)
        self.b9.grid(row = 3, column = 2,pady = 20)
        

    def winner(self):
        if self.b1['text'] == 'X' and self.b2['text'] == 'X' and self.b3['text'] == 'X':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'X Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 

        if self.b4['text'] == 'X' and self.b5['text'] == 'X' and self.b6['text'] == 'X':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'X Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 

        if self.b7['text'] == 'X' and self.b8['text'] == 'X' and self.b9['text'] == 'X':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'X Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 


        if self.b1['text'] == 'X' and self.b4['text'] == 'X' and self.b7['text'] == 'X':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'X Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 

        if self.b2['text'] == 'X' and self.b5['text'] == 'X' and self.b8['text'] == 'X':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'X Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 

        if self.b3['text'] == 'X' and self.b6['text'] == 'X' and self.b9['text'] == 'X':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'X Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 


        if self.b1['text'] == 'X' and self.b5['text'] == 'X' and self.b9['text'] == 'X':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'X Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20)

        if self.b3['text'] == 'X' and self.b5['text'] == 'X' and self.b7['text'] == 'X':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'X Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 
        




        if self.b1['text'] == 'O' and self.b2['text'] == 'O' and self.b3['text'] == 'O':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'O Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 

        if self.b4['text'] == 'O' and self.b5['text'] == 'O' and self.b6['text'] == 'O':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'O Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 

        if self.b7['text'] == 'O' and self.b8['text'] == 'O' and self.b9['text'] == 'O':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'O Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 


        if self.b1['text'] == 'O' and self.b4['text'] == 'O' and self.b7['text'] == 'O':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'O Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 

        if self.b2['text'] == 'O' and self.b5['text'] == 'O' and self.b8['text'] == 'O':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'O Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 

        if self.b3['text'] == 'O' and self.b6['text'] == 'O' and self.b9['text'] == 'O':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'O Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 


        if self.b1['text'] == 'O' and self.b5['text'] == 'O' and self.b9['text'] == 'O':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'O Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20)

        if self.b3['text'] == 'O' and self.b5['text'] == 'O' and self.b7['text'] == 'O':
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'O Wins',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 

       

    def btn_click1(self,event):
        self.b91.destroy()        
        global check
        check = check + 1       
        if check == 9:
            self.b91.destroy()
            self.b91 = Button(self.f2, text = 'TIED',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),bd = 0,command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20) 
        

        if self.pick_player == 1:
            self.pick_player = 2
                       
        else:       
            self.pick_player = 1
            
            
    def stop(self):
        quit()
    
    def start(self):        
        global check 
        check = 0
        
        self.l3.destroy()
        self.l4 = Message(self.f2,text = "",font = ('Arial',6),bg = 'black', anchor = N)        
        self.l4.grid(row = 5,column = 0,ipadx = 30,ipady = 30,pady = 40)
        
        
    def multi_func(self):
         
        self.clear()
        self.start()        
        self.new()
        self.flipcoin()
        
    def flipcoin(self):
        
        self.player = [1,2,2,1,1,2,2,1,1,2,2,1,1,2,2,1] 
        self.pick_player = random.choice(self.player)

        if self.pick_player == 1:
            self.b91 = Button(self.f2, text = 'O first',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20)
        if self.pick_player == 2:
            self.b91 = Button(self.f2, text = 'X first',bg = 'black',fg = 'yellow',font = ('Helvetica',15,'bold italic'),command = self.stop)
            self.b91.grid(row = 5,column = 0,pady = 20)
            
            
    def clear(self):
        self.b1 = Button(self.f1, text = " ",bg = 'white',        height = 3,width = 3)
        self.b1.grid(row = 1, column = 0,padx = 20,  pady = 20)
        self.b2 = Button(self.f1, text = " ",bg = 'white',        height = 3,width = 3)
        self.b2.grid(row = 1, column = 1,padx = 20,  pady =20)
        self.b3 = Button(self.f1, text = " ",bg = 'white',        height = 3,width = 3)
        self.b3.grid(row = 1, column = 2,padx = 20,  pady = 20)
        self.b4 = Button(self.f1, text = " ",bg = 'white',        height = 3, width = 3)
        self.b4.grid(row = 2, column = 0,pady = 20)
        self.b5 = Button(self.f1, text = " ",bg = 'white',        height = 3, width = 3)
        self.b5.grid(row = 2, column = 1,pady = 20)
        self.b6 = Button(self.f1, text = " ",bg = 'white',        height = 3,width = 3)
        self.b6.grid(row = 2, column = 2,pady = 20)
        self.b7 = Button(self.f1, text = " ",bg = 'white',        height = 3,width = 3)
        self.b7.grid(row = 3, column = 0,pady = 20)
        self.b8 = Button(self.f1, text = " ",bg = 'white',        height = 3,width = 3)
        self.b8.grid(row = 3, column = 1,pady = 20)
        self.b9 = Button(self.f1, text = " ",bg = 'white',        height = 3, width = 3)
        self.b9.grid(row = 3, column = 2,pady = 20)
       
    
    def widgets(self):

        self.l1 = Label(root,text = 'Tic-Tac-Toe',font = ('Arial',15,'italic'),bg = 'black', fg = 'white')
        self.l1.grid(row = 0, column = 0,padx = 195,pady = 10)

        self.f1 = Frame(root, bg = 'black')
        self.f1.grid(row = 1, column = 0)

        self.f2 = Frame(root, bg = 'black')
        self.f2.grid(row = 2, column = 0)
        
        

        self.l3 = Message(self.f2,text = ' ',font = ('Arial',6),bg = 'black', anchor = N)
        self.l3.grid(row = 5,column = 0,ipadx = 30,ipady = 30,pady = 40)
        

        self.b1 = Button(self.f1, text = "O",font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)
        self.b1.grid(row = 1, column = 0,padx = 20,pady = 20)

        self.b2 = Button(self.f1, text = "X",font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)
        self.b2.grid(row = 1, column = 1,padx = 20,pady =20)

        self.b3 = Button(self.f1, text = "O",font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)
        self.b3.grid(row = 1, column = 2,padx = 20,pady = 20)

        self.b4 = Button(self.f1, text = "X",font = ('Arial',9,'bold'),bg = 'white',height = 3, width = 3)
        self.b4.grid(row = 2, column = 0,pady = 20)

        self.b5 = Button(self.f1, text = "O ",font = ('Arial',9,'bold'),bg = 'white',height = 3, width = 3)
        self.b5.grid(row = 2, column = 1,pady = 20)

        self.b6 = Button(self.f1, text = " X",font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)
        self.b6.grid(row = 2, column = 2,pady = 20)

        self.b7 = Button(self.f1, text = "X",font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)
        self.b7.grid(row = 3, column = 0,pady = 20)

        self.b8 = Button(self.f1, text = "O",font = ('Arial',9,'bold'),bg = 'white',height = 3,width = 3)
        self.b8.grid(row = 3, column = 1,pady = 20)

        self.b9 = Button(self.f1, text = "X",font = ('Arial',9,'bold'),bg = 'white',height = 3, width = 3)
        self.b9.grid(row = 3, column = 2,pady = 20)

        self.b10 = Button(self.f2, text = 'Reset Board',font = ('Times',9,'bold italic'),bg = 'white',bd = 6,relief = RAISED,width = 15,command = self.multi_func)        
        self.b10.grid(row = 4,column = 0,pady = 20)

        self.b11 = Button(self.f2, text = 'Quit',bg = 'white',font = ('Helvetica',8,'bold italic'),bd = 3, relief = RAISED,command = self.stop)
        self.b11.grid(row = 6,column = 0,pady = 20)
        
        
textvar = StringVar()
check = 0

g = Game()
g.widgets()


root.mainloop()