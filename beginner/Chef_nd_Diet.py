for i in range(int(input())):
	s = list(map(int,input().split()))
	c = list(map(int,input().split()))
	j = 0
	for z in range(s[0]):
		j += c[z]
		if j < s[1]:
			print("NO {}".format(z+1))
			break
		j -= s[1]
	else:
		print("YES")
