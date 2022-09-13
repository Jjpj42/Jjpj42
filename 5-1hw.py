print (">> Program Find Maximum Digit <<")

while True :
    
    intNum = input("Enter integer number (0-Exit) : ")
    Max = int(intNum[0])

    #for find max
    for i in range (len(intNum)) :
        if(int(intNum[i]) > Max):
            Max = int(intNum[i])
    #end for
    #exit program
    if(intNum == "0") :
        print("Exit Program")
        break;
    print("Maximum Digi of integer number :",intNum," = ",Max)
