print (">> Program Find Maximim Digit <<")

Max = 0


def find_max(num):
    
    Number = int(num[0])
    
    for i in range(len(num)):
        if(int(num[i]) > Number):
            Number = int(num[i])

    return Number


while True:
    num = input ("Enter integer number(0-exit) : ")
    
    if(num == '0'):
        print ("Exit Program")
        break
    print (f"Maximum Digit of integer number : {num} = {find_max(num)}")
