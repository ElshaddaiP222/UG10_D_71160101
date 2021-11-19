b1 = int(input("masukan bilangan 1 : "))
b2 = int(input("masukan bilangan 2 : "))
b3 = int(input("masukan bilangan 3 : "))

bill1 = b1, b2, b3
bill2 = b1, b3, b2
bill3 = b2, b1, b3
bill4 = b2, b3, b1
bill5 = b3, b1, b2
bill6 = b3, b2, b1


if b1 > b2 and b1 > b3:
    if b2 > b3:
        print("urutan bilangan terbesar : ", bill1)
    else: print("urutan bilangan terbesar :", bill2)

elif b2 > b1 and b2 > b3:
    if b1 > b3:
        print("urutan bilangan terbesar :", bill3)
    else: print("urutan bilangan terbesar :", bill4)

else: 
    if b1 > b2:
        print("urutan bilangan terbesar : ", bill5)
    else: print("urutan bilangan terbesar :", bill6)


