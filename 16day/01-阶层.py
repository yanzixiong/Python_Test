#5! = 5*4*3*2*1
#4! = 4*3*2*1

'''
i = 1
a = 1
while i<=5:
	a*=i
	i+=1

print(a)
'''
def get_num(num):
	if num == 1:
		return 1
	else:
		return num*get_num(num-1)
print(get_num(5))

		
