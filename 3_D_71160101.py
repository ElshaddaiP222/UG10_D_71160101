belanja = str(input("masukan daftar belanjan anda : "))

print("daftar belanja : %s", % (belanja.title(), )

tambah = str(input("masukan barang yang ingin ditambahkan : "))

if tambah == belanja:
    print("barang %s", % (tambah.upper(), "sudah ada dalam daftar belanja")

else: print("hasil penambahan pada daftar belanja : ",belanja.title(), tambah.upper())
