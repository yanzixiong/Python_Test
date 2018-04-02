acc =input("请输入账号")
passwd = input("请输入密码")
need_money = input("请输入取款金额")
money = 5000
shengyu = money - need_money
if acc == "123456" and passwd == "111":
	print("开始取钱")
else:
	print("非法账户")
if money >= 100 and money <= 5000:
 	print("shengyu")
else:
	print("没钱去毛线")
