 #Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
#не превосходящие числа N.

number = int(input("Введите число: "))
level = 0

print ("Все степени двойки до числа", number,":")
for i in range(number):
    # for l in range ()
    level = pow(2, i)
    # print (level)
    if level < number:
        print (level)
