
import math

amount = int(input('Enter amount : '))
rate = float(input('Enter rate : '))
year = int(input('Enter year : '))
rate1 = rate/100
FV= float (amount*(1+rate1)**year)
print ("Future value = ",round(FV,2))
