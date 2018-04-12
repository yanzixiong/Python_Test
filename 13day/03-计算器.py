def jisuanqi(x,y,fuhao):
	if fuhao =="+":
		z = x+y
		print("和是%0.2f"%z)
	elif fuhao == "-":
		z= x-y
		print("差是%0.2f"%z)
	elif fuhao == "*":
		z = x*y
	
		print("积是%0.2f"%z)
	elif fuhao =="/":
		z = x/y
		if y!= 0:
			print("商是%0.2f"%z)
		else:
			print("输入有误")
x = float(input("请输入一个数字"))
y = float(input("请再输入一个数字"))
z = input("请输入一个符号+-*/")
jisuanqi(x,y,z)
