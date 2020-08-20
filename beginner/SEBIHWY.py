for m in range(int(input())):
    k, s, c, b, l = map(int, (input().split()))
    j = (180 * b / l) + k
    if abs(j - s) > abs(j - c):
        print("FATHER")
    elif abs(j - s) == abs(j - c):
        print("DRAW")
    else:
        print("SEBI")
