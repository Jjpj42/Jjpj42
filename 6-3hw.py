import random

ran = random.randint(1,99)
done = True
def check_int(num):
        if num < ran:
            print (f'! เลข {num} น้อยเกินไป')
            
        elif num > ran:
            print (f'! เลข {num} มากเกินไป')
            
        elif num == ran:
            print (f'\nถูกต้องครับ, เลขืี่สุ่มไว้คือ {ran}')
            done = False
            return done
            
        

print ("="*30)
print ("\tโปรแกรมเกมทายตัวเลข")
print ("="*30)

while done:
    
    num = int(input("ใส่ตัวเลขที่ต้องทาย : "))
    boolean = check_int(num)
    if(boolean == False):
        break
    

