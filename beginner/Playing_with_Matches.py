for i in range(int(input())):
    dic = {"0":6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}
    s = 0
    j, k = map(int, input().split())
    c = str(j + k)
    for i in c:
        s += dic[i]
    print(s)
