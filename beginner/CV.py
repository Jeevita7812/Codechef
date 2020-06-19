for i in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    for j in range(len(s)-1):
        if s[j] not in "aeiou":
            if s[j + 1] in "aeiou":
                c += 1
    print(c)
