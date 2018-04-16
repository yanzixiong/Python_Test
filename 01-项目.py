cards = []
idcard = []
def print_menu():
	print("学生成绩管理系统".center(30,"*"))
	print("1:录入成绩".center(30,"*"))
	print("2:查询成绩".center(30,"*"))
	print("3:删除成绩".center(30,"*"))
	print("4:修改成绩".center(30,"*"))
	print("5:打印全部成绩".center(30,"*"))
	print("6:退出系统".center(30,"*"))
def input_fun():	
	while True:
		fun_number = int(input("请选择功能"))
		if fun_number == 1:
			add_card()
		elif fun_number == 2:
			find_card()
		elif fun_number == 3:
			update_card()
		elif fun_number == 4:
			del_card()
		elif fun_number == 5:
			all_card()
		else:
			break
def add_card():		
		card = {}	
		name = input("请输入学生姓名")
		id_card = int(input("请输入学生学号"))
		c_chengji =int(input("请输入语文成绩"))
		m_chengji =int(input('请输入数学成绩')) 
		e_chengji = int(input("请输入英语成绩"))
		card['name'] = name
		card['id_card']= id_card
		card['c_chengji']= c_chengji
		card['m_chengji']= m_chengji
		card['e_chengji']= e_chengji
		cards.append(card)
		idcard.append(id_card)
		print("录入成功")
		print(cards)
def find_card():

		id_card = int(input("请输入学生号"))
		flag = 0#假设不在里面
		if id_card in idcard: 
		
			for temp in cards:
				if id_card == temp['id_card']:
					flag =1
					print('11111')
					print(temp['name'])
					print("姓名%s\n学号%d\n语文成绩%d数学成绩%d英语成绩%d"%(temp['name'],temp['id_card'],temp['c_chengji'],temp['m_chengji'],temp['e_chengji']))	
			
		else:
			print("信息有误")
		
def update_card():
	id_card = input("请输入学号")
	flag = 0
	for temp in cards:
		if id_card == temp['id_card']:
			flag = 1
			print("1:语文成绩".center(30," "))
			print("2:数学成绩".center(30," "))
			print("3:英语成绩".center(30," "))
			change_class = int(input("请输入要修改的课目成绩"))
			if change_class ==1:
				new_chengji = input("请输入新成绩")
				temp['c_chengji'] = nemw_chengji
			elif change_class ==2:
				new_chengji = input("请输入新成绩")
				temp['m_chengji'] = new_chengji
			elif change_class ==3:
				new_chengji = input("请输入新成绩")
				temp['e_chengji']= new_chengji

			else:
				print("输入有误")
def del_card():
	id_card =int(input("请输入学号"))
	flag = 0
	for temp in cards:
		if id_card  == temp['id_card']:
			flag =1
		sum_num = int(input('确定要删除嘛1:确定 2:返回'))
		if sum_num ==1:
			cards.remove(temp)
			print("删除成功")
		break
	if flag ==0:
		print("无法查询到该学号")
def all_card():
	print('姓名     学号       语文成绩     数学成绩    英语成绩')
	for temp in cards:
		print("%s\t%s\t%f\t%f\t%f\t"%(temp['name'],temp['id_card'],temp['c_chengji'],temp['m_chengji'],temp['e_chengji']))
print_menu()
input_fun()
	
