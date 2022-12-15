from random import randint
import time


def names():
    """Ввод имен"""
    gamer1 = input("Enter 1 player name:  ")
    gamer2 = input("Enter 2 player name:  ")
    return gamer1,gamer2


gamer1points = 0
gamer2points = 0
gamerdict = {}



for i in range(5):
    #Моделирование броска кубика 1 игроком 
    print("Кубик бросает", gamer1)
    time.sleep(2)
    n1 = randint(1,6)
    print("Выпало:  ", n1)
    gamer1points +=n1

    #Моделирование броска кубика 2 игроком 
    print("Кубик бросает", gamer2)
    time.sleep(2)
    n2 = randint(1,6)
    print("Выпало:  ", n2)
    gamer2points +=n2



def throw(gamer):
    print("Кубик бросает", gamer)
    time.sleep(2)
    n1 = randint(1,6)
    print("Выпало:  ", n1)
    return gamer1.points +=n1


    

    #Определение результата
    if n1 > n2:
        print("___Выиграл партию___: ", gamer1)
    elif n1< n2:
        print("___Выиграл партию___: ", gamer2)
    else:
        print("___Ничья___")




#Определение общего результата
if gamer1points > gamer2points:
    print("***Выиграл по сумме очков***: ", gamer1)
elif gamer1points < gamer2points:
    print("***Выиграл по сумме очков***: ", gamer2)
else:
    print("***Ничья, победила дружба***")

gamerdict[gamer1] = gamer1points
gamerdict[gamer2] = gamer2points
print(gamerdict)
with open("gameresult.txt", mode="a") as f:
    f.write(str(gamerdict))
for i in reversed(range(1,6)):
    print(i)
print("bye bye!")
time.sleep(3)
