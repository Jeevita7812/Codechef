for i in range(int(input())):
    n = int(input())
    r = 0
    while(n >= 100):
        r += 1
        n -= 100
    while(n >= 50):
        r += 1
        n -= 50
    while(n >= 10):
        r += 1
        n -= 10
    while(n >= 5):
        r += 1
        n -= 5
    while(n >= 2):
        r += 1
        n -= 2
    r += n
    print(r)
