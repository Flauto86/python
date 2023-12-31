# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих 
# чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

S = int(input("Введите сумму S: "))
P = int(input("Введите произведение P: "))

found = False

for X in range(1, 1001):
    Y = S - X  # Находим значение Y по сумме S и X
    if Y >= 1 and X * Y == P:  # Проверяем, что Y является натуральным числом и произведение равно P
        print("Задуманные числа: X =", X, ", Y =", Y)
        found = True
        break

if not found:
    print("Невозможно определить числа X и Y по заданным подсказкам.")
