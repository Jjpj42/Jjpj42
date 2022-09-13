print (">> Program Find Maximum Value <<")
value = int (input("Enter number of value(3-10) :"))

print ()

if(value < 3):
    value = 3
if(value > 10):
    value = 10
    
print ("Program get value",value,"number.")

i=0
numstr = ""
Max = 0

while i < value :
    i = i+1

    num = int(input(f"Enter value Number #{i}:"))
    if num > Max :
        Max = num
    if(i == value):
        numstr += str(num)
        break;
    numstr += str(num) + ", "
    
print ("Your enter number :",numstr)
print("Maximum value number is " ,Max)
print("Exit Program")

