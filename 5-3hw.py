print (">> Program Palindrome Number <<")


num = (input("Enter integer number : "))
num = str(num)
s = len(num)

if s[0] == s[-1]:
    print ('Digit',s[0],'equal to Digit',s[-1])

