hoten = input("Nhap ho va ten : ")
hoten = hoten.lower()
cactu = hoten.split()
hotenchuan = ""
for tu in cactu :
    tuchuan = tu[0].upper() + tu[1:len(tu)]
    hotenchuan += tuchuan + " "
print(f"Ho ten chuan : {hotenchuan}")