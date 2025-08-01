n = int(input("Nhap so luong phan tu : "))
a = []
for i in range(n) :
    num = str(input(f"a({i}) = "))
    a.append(num)
b = tuple(a)
print(b)
demso = 0
for tu in b :
    so = True
    if len(tu) == 0 :
        so = False
    else :
        for i in tu :
            if i not in '0123456789' :
                so = False
                break
    if so :
        demso += 1
print(f"co {demso} phan tu dang so")
