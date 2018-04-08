for i in range(2,101):
	b = 0
	for j in range(2,i):
		if i % j ==0:
			b=1
			break
	if b==0 :
		print(i)
