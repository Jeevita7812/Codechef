l = []
for i in range(int(input())):
     n = int(input())
     a = str(input()).split(" ")
     flag = 1
     count = 1
     a1 = n // 2 + 1
     for j in range(n):
         c = a[j]
         c = int(c)
         if(c != count):
             flag = 0
             break
         else:
             if(j < a1 - 1):
                 count += 1
             else:
                 count -= 1
     if(flag == 1 and count == 0):
         l.append("yes")
     else:
         l.append("no")
for i in l:
    print(i)
