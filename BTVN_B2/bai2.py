luong = int(input("Nhập lương của bạn(VND) : "))
if luong == 15000000:
    luong *= 0.7
elif luong < 15000000 and luong >= 7000000 :
    luong *= 0.8
elif luong < 7000000:
    luong *= 0.9
print("Sau khi trừ thuế số tiền bạn nhận được là : " , luong)