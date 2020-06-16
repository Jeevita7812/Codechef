for i in range(int(input())):
    n = int(input())
    guess = list(input().split())
    ans = list(input().split())
    marks = 0
    h = 0
    while h < n:
        if guess[h] == "N":
            marks = marks
        if guess[h] == ans[h]:
            marks += 1
            h += 1
        else:
            if guess[h] != ans[h] and guess[h] == "N":
                h += 2
    print(marks)
