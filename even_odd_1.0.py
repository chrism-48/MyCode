

#--Program to evaluate even or odd number.--

#--------------------------------------------
def even_or_odd():
    x = 1
    while x == 1:
        try:
            num = int(input("Enter a number: "))        
            if (num % 2) == 0:  
               print("{0} is Even number".format(num))
               x = 0
            else:  
               print("{0} is Odd number".format(num))
               x = 0
        except ValueError:
            print("Only enter numbers!")
            x = 1
            
       
#--------------------------------------------       
even_or_odd()        
run = True
while run:            
    ask = input("Again Yes(y) or No(n): ")
    try:
        if ask == 'y':
            run = True
            even_or_odd()
        if ask == 'n':
            run = False
            quit()
    except ValueError:
        continue
        
#-------------------------------------------        
            
