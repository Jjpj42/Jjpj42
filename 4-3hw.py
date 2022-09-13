'''
นายกิตติภพ เพชรบุรี
6506021620016
'''
print('>>Program Check Palindrome<<\n')

data = int(input('Enter integer number( 4 digit) : '))

if data // 1000 == data % 10 and data % 1000 // 100 == data % 100 // 10 :
    print("Your number is ",data," is palindrome")
else : print("Your number is" ,data," is not palindrome")
