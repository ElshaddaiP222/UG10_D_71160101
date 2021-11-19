makan = int(input("harga makan sebesar         : "))
snack = int(input("harga snack sebesar         : "))
minum = int(input("harga minum sebesar         : "))
uang  = int(input("uang yang anda bawa sebesar : "))

total = makan + snack + minum
kembalian = uang - total
utang = total - uang

print("Total yang anda harus bayar", total)

if uang == total:
    print("uang anda pas tidak ada kembalian")

if uang < total:
    print("uang anda tidak cukup anda masih mempunyai utang ", utang)

else: print("kembalian anda ", kembalian )