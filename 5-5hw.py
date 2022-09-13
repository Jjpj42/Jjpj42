print(">> Program Change Number ti Text <<")

number=int (input("Enter Integer number : "))

print(f"Number : {number}")

text=""

for i in str(number):
    if(i == '1'):
        text += "One "
    elif(i == '2'):
        text += "Two "
    elif(i == '3'):
        text += "Three "
    elif(i == '4'):
        text += "Four "
    elif(i == '5'):
        text += "Five "
    elif(i == '6'):
        text += "Six "
    elif(i == '7'):
        text += "Seven "
    elif(i == '8'):
        text += "Eight "
    elif(i == '9'):
        text += "Nine "
    elif(i == '0'):
        text += "Zero "

print(f"Text : {text}")
print("Exit Program")
