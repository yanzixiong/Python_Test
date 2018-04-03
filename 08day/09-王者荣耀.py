s_acc = "yzx"
s_pwd = "123456"
count = 0
while True:
	acc = input("请输入账号")
	pwd = input("请输入密码")
	if acc == s_acc and pwd ==s_pwd:
		hero = int(input("请选择英雄:ADC---0  肉---1  法师---3"))
		if hero == 0:
			print("鲁班大师")
		elif hero == 1:
			print("程咬金")
		elif hero ==3:
			print("王昭君")

		break
	else:
		count+=1
		print("erroe%d次"%count)
		if count==3:
			print("账号冻结")
			break
	



