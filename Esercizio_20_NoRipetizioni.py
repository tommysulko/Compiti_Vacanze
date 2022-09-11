def is_isogram(string):
    string = string.upper().replace("-","").replace(" ","")
    cont = 0
    for i in string:
        cont = 0
        for k in string:
            if k == i:
                cont += 1
        if cont > 1:
            return False
    return True