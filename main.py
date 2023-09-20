import math
from math import factorial

def f(val):
    if val is None:
        return False
    try:
        float(val)
        return True
    except ValueError:
        return False

action = '0'
while action != '11':
    result = 0
    print("Выберите действие:"
          "\n1. Сложение"
          "\n2.Вычитание"
          "\n3.Умножение"
          "\n4.Деление"
          "\n5.Возвести первое число в n степень"
          "\n6.Факториал первого числа"
          "\n7.Синус первого числа"
          "\n8.Косинус первого числа"
          "\n9.Тангенс первого числа"
          "\n10.Квадратный корень первого числа"
          "\n11.Выйти из программы")
    action = input()

    print("Введите первое число:")
    user_num1 = input()
    print("Введите второе число")
    user_num2 = input()

    if f(user_num1) and f(user_num2):
        user_num1 = float(user_num1)
        user_num2 = float(user_num2)
    else:
        print("Введите число!!!")
        continue


    num_factorial = str(user_num1)
    num_factorial = num_factorial.split('.')

    if action == '1':
        result = user_num1 + user_num2


    elif action == '2':
        result = user_num1 - user_num2


    elif action == '3':
        result = user_num1 * user_num2


    elif action == '4':
        if user_num2 == 0:
            print('ERROR, на ноль делить нельзя!')
            continue
        else:
            result = user_num1 / user_num2


    elif action == '5':
        print("Введите в какую степень возвести")
        user_num3 = input()
        if f(user_num3):
            user_num3 = float(user_num3)
            result = user_num1 ** user_num3
        else:
            print("ERROR, Введено не число")
            continue


    elif action == '6':
        if user_num1 < 0 or num_factorial[1] != '0':
            print('ERROR, Факториал можно вычеслить из целого числа большего нуля')
            continue
        else:
            user_num1 = int(user_num1)
            result = factorial(user_num1)


    elif action == '7':
        result = math.sin(user_num1)


    elif action == '8':
        result = math.cos(user_num1)


    elif action == '9':
        result = math.tan(user_num1)


    elif action == '10':
        if user_num1 < 0:
            print("Корней из отрицательного числа не бывает!")
        else:
            result = math.sqrt(user_num1)


    else:
        print("ERROR, введите корректное дейсвтие!!!")
        continue

    print("Выш результат - ", result)

    print("Нажмите 0 чтобы завершить, 1 чтобы продолжить")
    user_input = input()
    if user_input == '0':
        break
    else:
       pass
