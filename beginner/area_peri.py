l = int(input())
b = int(input())
area = l*b
peri = 2*(l + b)
if area > peri:
    print("Area")
    print(area)
elif peri > area:
    print("Peri")
    print(peri)
else:
    print("Eq")
    print(area or peri)
