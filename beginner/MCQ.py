for i in range(0,int(input())):
    n = int(input())
    m = input()
    o = input()
    marks = 0
    i = 0
    while(i < n):
        if(m[i] == o[i]):
            marks += 1 
        elif(o[i] == 'N'):
            marks += 0 
        elif(m[i] != o[i] and o[i]!='N'):
            if(i == n - 1):
                i += 0
            else:
                i += 1
                marks += 0
        i += 1
    print(marks)
