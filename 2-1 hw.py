

money = float(input("Enter number money withdraw : "))

print ()

B1000 = money // 1000
print ("Cash B1000 : ",B1000)
B500 = money % 1000
B5 = B500 // 500
print ("Cash B500 : ",B5)
B100 = money % 500
B1 = B100 // 100
print ("Cash B100 : ",B1)
