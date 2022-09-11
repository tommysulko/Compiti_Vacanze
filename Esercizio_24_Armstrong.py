def is_armstrong_number(number):
    num = str(number)
    somma = 0
    for cifra in num:
        somma += int(cifra) ** len(num)
    if somma == number:
        return True
    return False