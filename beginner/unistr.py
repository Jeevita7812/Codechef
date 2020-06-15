t = int(input())
for i in range(t):
    n = input()
    m = 0
    n = n.strip()
    for j in range(len(n)-1):
        if int(n[j])!=int(n[j+1]):
            m = m + 1
    if n[0] != n[len(n)-1]:
        m = m + 1 
    if m <= 2:
        print('uniform')
    else:
        print('non-uniform')
