for i in range(int(input())):
    dic = {"cakewalk":0, "simple":0, "easy":0, "easy-medium":0, "medium":0, "medium-hard":0, "hard":0}
    for k in range(int(input())):
        j = input().strip()
        if j in dic:
            dic[j] = dic[j] + 1
    if dic["cakewalk"] == 0:
        print("No")
        continue
    if dic["simple"] == 0:
        print("No")
        continue
    if dic["easy"] == 0:
        print("No")
        continue
    if dic["easy-medium"] == 0 and dic["medium"] == 0:
        print("No")
        continue
    if dic["medium-hard"] == 0 and dic["hard"] == 0:
        print("No")
        continue
    else:
        print("Yes")
