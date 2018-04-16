cards = []
def print_menu():
	print("名片系统v1.0版本".center(30,"*"))
	print("1:新增名片".center(30," "))
	print("2:查找名片".center(30," "))
	print("3:修改名片".center(30," "))
	print("4:删除名片".center(30," "))
	print("5:全部名片".center(30," "))
	print("6:退出系统".center(30," "))
def input_fun ():	
	while True:
		fun_number = int(input("请选择功能"))
		if fun_number ==1:
			add_card()
		elif fun_number == 2:
			find_card()
		elif fun_number ==3:
			update_card()
		elif fun_number ==4:
			del_card()
		elif fun_number ==5:
			all_card()
		else:
			break
def add_card():
	card={}
	name = input("请输入名字")
	job = input("请输入职位")
	phone = int(input("请输入手机号"))
	company = input("请输入公司名字")
	address = input("请输入公司地址")
	card["name"] = name
	card["job"]  = job
	card["phone"] = phone
	card["company"] = company
	card["address"] = address
	cards.append(card)
	print("新增成功\n")
	print(cards)
def find_card():
	name = input("请输入要查的姓名")
	flag = 0 #假设不在里面
	for temp in cards:
		if name == temp['name']:
			print("姓名:%s\n职位:%s\n手机号:%s\n公司:%s\n地址:%s\n"%(temp['name'],temp['job'],temp['phone'],temp['company'],temp['address']))
			flag = 1

	if flag == 0:
		print("查无此人\n")	
def update_card():
	name  = input("你输入要修改的名字")
	flag = 0
	for temp in cards:
		if name == temp["name"]:
			flag = 1
			print("1:修改名字".center(30," "))
			print("2:修改职位".center(30," "))
			print("3:修改手机号".center(30," "))
			print("4:修改公司名称".center(30," "))
			print("5:修改公司地址".center(30," "))
			change_num = int(input("请选择修改序号"))
			if change_num == 1:
				new_name = input("请输入新的名字")
				temp["name"] = new_name
			elif change_num == 2:
				new_job = input("请输入新的职位")
				temp["job"] = new_job
			elif change_num == 3:
				new_phone = int(input("请输入手机号"))
				temp["phone"] = new_phone
			elif change_num == 4:
				new_company = input("请输入新的公司名")
				temp["company"] = new_company
			elif change_num == 5:
				new_address = input("请输入新的地址")
				temp["address"] = new_address
			else:
				print("输入有误\n")
def del_card():		
		name = input("请输入要删除的名字")
		flag = 0 #假设默认不存在
		for temp in cards:
			if name == temp["name"]:
				flag = 1
				sure_num = int(input("确定要删除吗1:确定 2:返回"))
				if sure_num == 1:
					cards.remove(temp)
					print("删除成功")
				break
		if flag == 0:
			print("没有此人")	
def all_card():
	print('名    字 职位    手机号   公司名字    公司地址 ')
	for temp in cards:
		print("%s\t%s\t%s\t%s\t%s\t"%(temp['name'],temp['job'],temp['phone'],temp['company'],temp['address'])) 
	
print_menu()
input_fun()
