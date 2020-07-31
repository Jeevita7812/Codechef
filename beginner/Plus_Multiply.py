for i in range(int(input())):
    zy = int(input())
    js = list(map(int, input().split()))
    b = js.count(0) * (js.count(0) - 1) // 2
    cl = js.count(2) * (js.count(2) - 1) // 2
    print(b + cl)
