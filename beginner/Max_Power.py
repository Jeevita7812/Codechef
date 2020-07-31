n = int(input())
s = input()
l = list(s)
c = n - 1
j = 0
while (c >= 0):
    if l[c]=='0':
        j += 1 
        c -= 1
    else:
        break 
print(j)
