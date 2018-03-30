account = input("请输入您的账号")
password = input("请输入您的密码")
name = input("请输入名字")
money = 200000000#原有的存款
need_money = input("请输入您要取得金额")
sum = money - int(need_money)
print("账号:%s\n密码:%s名字:%s\n原有的存款:%d\n取款金额:%s\n剩余:%d"%(account,password,name,money,need_money,sum))
