# Giải phương trình bậc 2
import math

print("Nhap gia tri a: ",end="")
a = int(input())
print("Nhap gia tri b: ",end="")
b = int(input())
print("Nhap gia tri c: ",end="")
c = int(input())

def phuongtrinhbac2(a,b,c):
    delta = b*b - 4*a*c
    if (delta > 0):
        x1 = (-b + math.sqrt(delta)) // 2*a  # "//" is integer division ****  "/" is float division
        x2 = (-b - math.sqrt(delta)) // 2*a
        print(f"\nPhuong trinh co 2 nghiem phan biet la: \nx1 = {x1}\nx2 = {x2}.")
    elif (delta == 0):
        x = -b / 2*a
        print(f"\nPhuong trinh co nghiem kep x1 = x2 = {x}.")
    else:
        print("\nPhuong trinh vo nghiem.")

phuongtrinhbac2(a,b,c)
