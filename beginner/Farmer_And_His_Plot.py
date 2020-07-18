for i in range(int(input())):
    j, s = map(int, input().split())
    cy = 0
    if j <= s:
        cy = j
    else:
        cy = s
    for k in range(1, cy + 1):
        if j % k == 0 and s % k == 0:
            zy = k
    print(int((j * s) / (zy * zy)))
