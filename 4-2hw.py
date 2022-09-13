
print('>>Program Find Maximum Value<<\n')

num1 = int(input('Enter number 1 : '))
num2 = int(input('Enter number 2 : '))
num3 = int(input('Enter number 3 : '))
num4 = int(input('Enter number 4 : '))
num5 = int(input('Enter number 5 : '))

print(f'Your enter number {num1},{num2},{num3},{num4},{num5}')
if (num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5):
     n = num1
if (num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5):
     n = num2
if (num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5):
     n = num3
if (num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5):
     n = num4
if (num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4):
     n = num5
print ("Maximum number is",n)
