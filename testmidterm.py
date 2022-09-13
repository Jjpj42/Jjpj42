print("="*40)
print("       Program Calculate Grade          ")
print("="*40)

i = 1
text = []
textCredit=[]
textGrade=[]
textLevel=[]
textPoint=[]
total = totalPoint = 0
while i < 6 :
    Score = int(input(f"Enter Score {i} : "))
    Credit = int(input(f"Enter Credit {i} : "))
    if(Score <=100):
        Grade = "A"
        Level = 4
    if(Score <=79):
        Grade = "B+"
        Level = 3.5
    if(Score <=74):
        Grade = "B"
        Level = 3
    if(Score <=69):
        Grade = "C+"
        Level = 2.5
    if(Score <=64):
        Grade = "C"
        Level = 2
    if(Score <=59):
        Grade = "D+"
        Level = 1.5
    if(Score <=54):
        Grade = "D"
        Level = 1
    if(Score <=49):
        Grade = "F"
        Level = 0

    total += Credit
    totalPoint += (Level*Credit)
    
    text.append(Score)
    textCredit.append(Credit)
    textGrade.append(Grade)
    textLevel.append(Level)
    textPoint.append(Level*Credit)
    i+=1

    
print("="*50)
print("                    Report Grade        ")
print("="*50)
print("| No .  | Score | Grade | Level  | Credit   | Point  |")

'''print(f" 1     |   {text[0] +text[1]}  |   {textGrade[0]}   |    |  {textCredit[0]}  |      | ")
print(f" 2     |   {text[2] +text[3]}  |   {textGrade[1]}   |     |  {textCredit[1]}  |      | ")
print(f" 3     |   {text[4] +text[5]}  |   {textGrade[2]}   |     |  {textCredit[2]}  |      | ")
print(f" 4     |   {text[6] +text[7]}  |   {textGrade[3]}   |     |  {textCredit[3]}  |      | ")
print(f" 5     |   {text[8] +text[9]}  |   {textGrade[4]}   |     |  {textCredit[4]}  |      | ")'''

i=0
done = True
while done :
    print(f"  {i+1}     |   {text[i]}  |   {textGrade[i]}   |   {textLevel[i]}    |  {textCredit[i]}       |   {textPoint[i]}    | ")
    
    i+=1
    if(i == 5):
        break
print(f"|                 Total               |    {total}    |    {totalPoint}   |")