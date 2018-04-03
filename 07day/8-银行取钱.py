iaccout = "123456"
passwd = "111111"
money = 50000
s_accout = input("请输入账户")
s_passwd = input("请输入密码")
if s_accout == iaccout and s_passwd == passwd:
	q_money = float(input("请输入取钱金额"))
	if money < q_money:
		print("没钱取毛线")
	else:
	   	print("取了%f钱，还剩%f钱"%(q_money,money-q_money))
else:
		print("非法账户")
