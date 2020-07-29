for i in range(int(input())):
  j, s = map(int, input().split())
  if((j * s) % 2 == 0):
    print("YES")
  else:
    print("NO")
