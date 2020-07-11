s = input()
c = 0
h = 0
e = 0
f = 0
for j in s:
    if(j == 'C'):
        c += 1
    elif(j == 'H' and c > h):
        h += 1
    elif(j == "E" and h > e):
        e += 1
    elif(j == 'F' and e > f):
        f += 1
print(f)
