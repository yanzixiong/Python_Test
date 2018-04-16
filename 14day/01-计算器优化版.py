'''
def jisuanqi(a,b):

	z = a + b 
	j = a - b
	m = a*b
	n = a/b
	return z,b ,m,n

z,j,m,n = jisuanqi(1,2)	
print(z,j,m,n)
'''
def jisuanqi(a,b,fuhao):
	if fuhao == "+":
		z = a+b
	elif fuhao == "-":
		z = a-b
	elif fuhao == "*":
		z = a*b
	elif fuhao =="/":
		z = a/b
	return z
while True:
	a = float(input("请输入一个数字"))
	b = float(input("请输入一个数字"))
	fuhao = input("请输入符号+,-,*,/")	

	z = jisuanqi(a,b,fuhao)
	print(z)
	
