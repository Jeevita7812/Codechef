for i in range(int(input())):
    n = int(input())
    s = ''
    for k in range(n):
        t = input()
        s = s + t 
    j = list(s)
    c = min(j.count('c') // 2, j.count('o'), j.count('d'), j.count('e') // 2, j.count('h'), j.count('f'))
    print(c)
