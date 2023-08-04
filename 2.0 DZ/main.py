# : На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. Выведите минимальное количество монет, 
#которые нужно перевернуть

import random
emblem = 0
reshka = 0
monety = int(input("Введите количество монеток: "))
array = []*monety
sides = random.randint(0, 1)
for i in range(monety):
    sides = random.randint(0, 1)
    array.append(sides)
    if sides == 1:
        emblem += 1
    else:
        reshka += 1
if  emblem > reshka:
    print (array) 
    print ("Нужно перевернуть", reshka, "решка(и)")
else:
    print ("Нужно перевернуть", emblem, "герб(а)")    
