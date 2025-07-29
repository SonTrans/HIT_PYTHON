s1 = input("s1 : ")
s2 = input("s2 : ")
daonguocs1 = ""
for i in range(len(s1)-1,-1,-1 ) : 
    daonguocs1 += s1[i]
print(f"s1 sau khi dao nguoc la : {daonguocs1}")
a = int(input("Nhap so a : "))
b = int(input("Nhap so b : "))
daonguocs2 = ""
dau = ""
for i in range(a-1) :
    dau += s2[i]
giua = ""
for i in range(b-1,a-2,-1) :
    giua += s2[i]
cuoi = ""
for i in range(b,len(s2)) :
    cuoi += s2[i]
print(f"s2 sau khi chinh sua : {dau+giua+cuoi}")
s3 = ""
for i in range(len(s1)):
    if i % 2 != 0:  
        s3 += s1[i]
print(f"s3 : {s3}")
s4 = ""
for i in range(len(s1) + len(s2)) :
    if i < len(s1) :
        s4 += s1[i]
    if i < len(s2) :
        s4 += s2[i]
print(f"s4 : {s4}")

 

