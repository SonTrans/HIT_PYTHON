n = int(input("Nhap so luong phan tu : "))
a = []
for i in range(n) :
    num = int(input(f"a[{i}] = "))
    a.append(num)
x = int(input("Nhap so can ktra : "))
demso = 0
for num in a :
    if num == x :
        demso += 1
print(f"phan tu {x} xuat hien {demso} lan")
lstmoi = [8,5,4,0,1,3]
a[2:8] = lstmoi
print("list moi : ", a)
max = a[0]
min = a[0]
for num in a :
    if num > max :
        max = num
    if num < min :
        min = num
print(f"gia tri lon nhat la : {max}")
print(f"gia tri nho nhat la : {min}")
y = int(input("Nhap so y : "))
a.insert(0,y)
print(a)
tang = True
giam = True
for i in range(len(a) - 2) :
    if a[i] < a[i+1] :
        giam = False
    if a[i] > a[i+1] :
        tang = False 
    if not a[i] > a[i+1] and a[i] < a[i+1] :
        break
if tang :
    print("Tang")
elif giam :
    print("Giam")
else :
    print("No")
        

 