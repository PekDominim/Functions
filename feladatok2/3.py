def harommal_oszthatok(szam):
    szam = len([i for i in szam if i%3==0])
    return szam
print(harommal_oszthatok(range(1, 999999 )))
