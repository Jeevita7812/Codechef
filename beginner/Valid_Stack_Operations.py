for i in range(int(input())):
	b = int(input())
	s = 0
	j = 0
	c = input().split()
	for k in range(b):
		if c[k] == "1":
			j += 1
		elif c[k] == "0":
			j -= 1
			if j < 0:
				s = 1
				break
	if s == 1:
		print('Invalid')
	else:
		print('Valid')
