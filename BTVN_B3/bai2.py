k = int(input("Nhap so luong phan tu : "))
a = []
for i in range(k) :
    num = int(input(f"a[{i}] = "))
    a.append(num)
n = int(input("Nhap so dong cua ma tran : "))
m = int(input("Nhap so cot cua ma tran : "))
for i in range(len(a)) :
    if n*m <= k :
        star = m*i
        end = m*(i+1)
        if end > len(a) :
            break
        print(a[star : end])
    else : 
        print ("No")
        break

