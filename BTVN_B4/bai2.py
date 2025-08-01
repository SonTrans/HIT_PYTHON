n = int(input("Nhap so luong sv dki ban 1 : "))
a = []
for i in range(n) :
    num1 = str(input(f"a({i}) = "))
    a.append(num1)
m = int(input("Nhap so luong sv dki ban 2  : "))
b = []
for i in range(m) :
    num2 = str(input(f"b({i}) = "))
    b.append(num2)
A = set(a)
B = set(b)
print(type(A))
print("Cac sv dki tai ban 1 : ", A )
print("Cac sv dki tai ban 2 : ", B)
ktra = A.isdisjoint(B)
if ktra == True:
    print("Khong co sv nao dki tai ca 2 ban")
else :
    chung = A.intersection(B)
    print(f"Cac sv dki tai ca 2 ban la : {chung}" )
svban1 = A.difference(B)
print(f"Cac sv chi dang ki tai ban 1 la : {svban1}")