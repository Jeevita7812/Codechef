t = int(input())
for i in range(t):
    n = input()
    if n == 'b' or 'B':
        print('BattleShip')
    elif n == 'c' or 'C':
        print('Cruiser``')
    elif n == 'd' or 'D':
        print('Destroyer')
    elif n == 'f' or 'F':
        print('Frigate')
