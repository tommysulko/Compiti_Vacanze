def square(number): 
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    return 2**(number-1)


def total():
    somma = 0
    for n in range(1, 65):
        somma += square(n)
    return somma