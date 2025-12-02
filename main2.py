a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
sign = input("Введите знак операции (+, -, *, /, //, %, **): ")

valid_ops = ['+', '-', '*', '/', '//', '%', '**']

if sign not in valid_ops:
    print("Ошибка: неизвестная операция!")
else:
    result = None

    if sign == '+':
        result = a + b
    elif sign == '-':
        result = a - b
    elif sign == '*':
        result = a * b
    elif sign == '/':
        if b != 0:
            result = a / b
        else:
            result = "Ошибка: деление на ноль!"
    elif sign == '//':
        if b != 0:
            result = a // b
        else:
            result = "Ошибка: деление на ноль!"
    elif sign == '%':
        if b != 0:
            result = a % b
        else:
            result = "Ошибка: деление на ноль!"
    elif sign == '**':
        result = a ** b

    if result is not None:
        print("Результат:", result)
    else:
        print("Неизвесная ошибка: результат не вычислен")


