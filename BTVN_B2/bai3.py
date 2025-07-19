n = int(input("Nhập số nguyên n : "))
count = 0
sum = 0
sobandau = n
while n > 0:
    socuoi = n % 10
    sum += socuoi
    count += 1
    n //= 10
    if socuoi == 0:
        break
print("Số ban đầu có : " , sobandau)
print("có " , count , " chữ số ")
print("Có tổng các chữ số là : ", sum)