thang = int(input("Nhập tháng : "))
nam = int(input("Nhập năm : "))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang ==12:
    ngay = 31 
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    ngay = 30
elif thang == 2 :
    if nam % 4 == 0:
        ngay = 29
    else :
        ngay = 28
print(ngay)