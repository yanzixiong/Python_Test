def sushu():
	for i in range(100,201):
		b = 0
		for j in range(2,i):
			if i % j == 0:
				b=1
				break
		if b ==0:
			print(i)
sushu()
