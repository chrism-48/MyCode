print("")
print("Manual concentrate converter")
print("----------------------------------")
print("")
mat = input("Enter material weight in lbs: ")

conc = input("Enter concentrate letdown ratio in percent: ")

print("")
if conc == '2':
    conc2 = float(.02)
if conc == '8':
    conc2 = float(.08)
    
    
    

figure1 = float(mat)
figure2 = float(conc2)

ans = (figure1 * figure2)
print (str(ans) + " lb(s) of concentrate.")
print("")
ender = input("Press enter to close: ")