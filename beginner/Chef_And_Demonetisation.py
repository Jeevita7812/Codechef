for i in  range(int(input())):
	s, c = map(int, input().split(" "))
	j = 0
	j = j + (s // c)
	if s % c == 0:
		print(j)
	elif s % c == 1:
		j += 1
		print(j)
	else:
		 if (s % c) % 2 == 0:
		 	j += 1
		 	print(j)
		 else:
		 	j += 2
		 	print(j)
