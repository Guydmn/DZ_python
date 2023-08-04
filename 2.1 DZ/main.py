# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных 
# числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает 
# две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

sum = int(input("Введите сумму чисел: "))
multiplication = int(input("Введите произведение чисел: "))
i = 1
number1 = 0
number2 = 0
checking = 0
for i in range(1, multiplication):
    checking = (multiplication/i)+i
    if checking == sum:
        number1 = multiplication/i
        number2 = i
        print ("Первое число - ", number1, "Второе число - ", number2)
        break
