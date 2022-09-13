import random

print ("="*30)
print ("\tโปรแกรมเกมทายตัวเลข")
print ("="*30)

random = random.randint(1,99)

num = 0

while True:
    num = int (input("ใส่ตัวเลขที่ต้องทาย = "))
    if num < random :
        print (f"! เลข {num} น้อยเกินไป")
    if num > random :
        print (f"! เลข {num} มากเกินไป")
    if num == random :
        print (f"ถูกต้องครับ, เลขที่สุ่มไว้คืิอ {random}")
        break
