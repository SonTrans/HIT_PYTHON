a = input("Nhap vao day ki tu : ").split()
b = set()
for i in a:
    for kitu in i:
        b.add(kitu)
kq = list(b)
print(kq)