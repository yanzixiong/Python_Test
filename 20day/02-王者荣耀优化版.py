list = [] #储存账号

def  register():

	account,pwd = cus_input()

	#判断账号存在不存

	#在 返回字典

	#不在 返回None

	temp= check_account(account)

	if temp == None:

		dict = {}

		dict["account"] = account

		dict["pwd"] =pwd

		list.append(dict)

		print("注册成功")

	else:

		print("账号存在")

def login():

	account,pwd = cus_input()

	temp = check_account(account)

	if temp != None:

		if temp.get("status") == 1:#账号在登录

			print("账号在登录着")

		else:

			if pwd == temp["pwd"]:

				print("登录成功")

				temp["status"] = 1 #1代表登录 0代表未登录

			else:

				print("密码不对")

	else:

		print("账号不存在，请先注册")



def loginout():

	account = input("请输入账号")

	temp = check_account(account)

	if temp != None:

		if temp.get("status") == 1:

			print("账号退出成功")

			temp["status"] = 0

		else:

			print("sb")

	else:

		print("账号不存在")



#输入菜单

def cus_input():

	account = input("请输入账号")

	pwd = input("请输入密码")

	return account,pwd



#用来检测账号是否存在

def check_account(account):

	flag = 0

	for i in list:

		if account == i["account"]:

			flag = 1 #在的话返回1

			return i #把字典返回过去

			#break



	if flag == 0:

		return None #不在返回0



					

while True:

	fun= int(input("请选择功能 1注册 2登录 3登出 4退出"))

	if fun == 1:

		register()

	elif fun == 2:

		login()

	elif fun  == 3:

		loginout()
