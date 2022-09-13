print (">> Program Change Number to Text <<")

def num_to_text(num):
    text = ""
    for i in str(num):
        
        if (i == "1"):
            text += "One "
        elif (i == "2"):
            text += "Two "
        elif (i == "3"):
            text += "Three "
        elif (i == "4"):
            text += "Four "
        elif (i == "5"):
            text += "Five "
        elif (i == "6"):
            text += "Six "
        elif (i == "7"):
            text += "Seven "
        elif (i == "8"):
            text += "Eight "
        elif (i == "9"):
            text += "Nine "
        elif (i == "0"):
            text += "Zero "
    return text

num = int(input("Enter integer number : "))
number = num_to_text(num)
print (f'Number : {num}')
print (f'Text : {number}')
print ("Exit Program")
