n = int(input("Nhap so luong phan tu : "))
a = []
for i in range(n) :
    num = str(input(f"a({i}) = "))
    a.append(num)
A = tuple(map(int , a))
sum = 0
for i in range(len(A)) :
    sum += A[i]
print(f"Trung binh cong cac phan tu : {sum/n}")
