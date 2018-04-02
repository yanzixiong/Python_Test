acc = input("请输入账号")
passwd = input("请输入密码")

if acc == "123456" and passwd == "abc":
	print("登录成功")
elif acc == "123456" and passwd !="abc":
	print("密码不对")
elif acc != "123456" and passwd == "abc":
	print("账号不对")
else:
	print("登录失败")
