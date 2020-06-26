for i in range(int(input())):
    js = input().split()
    zl = 0
    for cy in js:
        if cy == '1':
            zl += 1
    if zl == 0:
        print("Beginner")
    elif zl == 1:
        print("Junior Developer")
    elif zl == 2:
        print("Middle Developer")
    elif zl == 3:
        print("Senior Developer")
    elif zl == 4:
        print("Hacker")
    else:
        print("Jeff Dean")
