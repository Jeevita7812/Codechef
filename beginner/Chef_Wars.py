c = int(input())
bk = 1
while bk <= c:
    s, j = map(int, input().split())
    while True:
        s -= j
        j /= 2
        if s <= 0:
            print("1")
            break
        elif j < 1:
            print("0")
            break
    bk += 1
