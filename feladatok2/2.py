def paros_e(szam):
    for i in szam:
        if i%2 == 0:
            return True
    return False
print(paros_e([1, 2, 3, 4]))
