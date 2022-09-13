
print (">>Program Find Maximum Digit<<\n")
Number = input("Enter integer number(4 digit) : ")

Num = len(Number)

if(Num == 4):
    
    if(int(Number[0])>int(Number[1])):
        Max = Number[0]
    elif(int(Number[1])>int(Number[2])):
        Max = Number[1]
    elif(int(Number[2])>int(Number[3])):
        Max = Number[2]
    elif(int(Number[3])>int(Number[0])):
        Max = Number[3]   
    elif(int(Number[2])>int(Number[1])):
        Max = Number[2]
else :
    print("Error Please Input Number (4 digit)")


print(f"Maximum Digit if Integer number {Number} = {Max}")


