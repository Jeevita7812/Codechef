t = int(input())
n = input().split()
eve_num = 0
odd_num = 0
for slj in n:
    slj = int(slj)
    if slj % 2 == 0:
        eve_num = eve_num + 1
    else:
        odd_num = odd_num + 1
if eve_num > odd_num:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
