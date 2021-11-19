a = float(input("nilai a : "))
b = float(input("nilai b : "))
c = float(input("nilai c : "))

rumus = (b**2) - (4*a*c)
rumus2 = (-b + rumus) / (2*a)
rumus3 = (-b - rumus) / (2*a)

if rumus > 0:
         print("akar dari persamaan tersebut adalah", rumus2, "dan", rumus3)

elif rumus < 0:
        print("Fungsi tidak memiliki angka rill")

else: 
    if rumus == 0:
        print("fungsi memiliki akar kembar yaitu ", rumus3)
