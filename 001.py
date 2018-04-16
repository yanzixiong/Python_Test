cards = []
idcard = []
def menu():
	print("学生成绩管理系统".center(30,"*"))
	print("1:录入成绩".center(30,"*"))
	print("2:查询成绩".center(30,"*"))
	print("3:删除成绩".center(30,"*"))
	print("4:修改成绩".center(30,"*"))
	print("5:打印全部成绩".center(30,"*"))
	print("6:退出系统".center(30,"*"))
def addCard():
	name = input('请输入姓名')
	num = int(input('请输入学号'))
	chinese = int(input('请输入语文成绩'))
	math = int(input('请输入数学成绩'))
	english = int(input('请输入英语成绩'))
	if num in idcard:
		print('学号已存在')
	else:
		print('添加成功')
		dic = {}
		dic['name'] = name
		dic['num'] = num
		dic['chinese'] = chinese
		dic['math'] = math
		dic['english'] = english
		cards.append(dic)
		idcard.append(num)
def findCard():
	nums = int(input('输入要查询的学号'))
	if nums in idcard:
		for temp in cards:
			if nums == temp['num']:
				sub = input('请输入要查询的课目语文数学英语')
				if sub == '语文':
					print('您要查询的姓名为%s，学号为%d，语文成绩为%d'%(temp['name'],temp['num'],temp['chinese']))
				elif sub == '数学':
					print('您要查询的姓名为%s，学号为%d，数学成绩为%d')
				elif sub == '英语':
					print('您要查询的姓名为%s，学号为%d，英语成绩为%d')
				else:
					print("姓名%s\n学号%d\n语文成绩%d数学成绩%d英语成绩%d"%(temp['name'],temp['num'],temp['chinese'],temp['math'],temp['english']))	
			else:
				continue
	else:
		print('学号输入错误')
def delCard():
	nums = int(input('输入要删除的学号'))
	if nums in idcard:
		for temp in cards:
			if nums == temp['num']:
				cards.remove(temp)
				idcard.remove(nums)
				print('删除成功')
			else:
				continue
	else:
		print('学号输入错误')
def updateCard():
	nums = int(input('输入要修改的学号'))
	if nums in idcard:
		for temp in cards:
			if nums == temp['num']:
				sub = input('请输入要修改的课目')
				if sub == '语文':
					new = int(input('请输入新的成绩'))
					temp['chinese'] = new
					print('修改成功')
				elif sub == '数学':
					new = int(input('请输入新的成绩'))
					temp['chinese'] = new
					print('修改成功')
				elif sub == '英语':
					new = int(input('请输入新的成绩'))
					temp['chinese'] = new
					print('修改成功')
			else:
				continue
	else:
		print('学号输入错误')
def allCard():
	for temp in cards:
		print("姓名%s\n学号%d\n语文成绩%d数学成绩%d英语成绩%d"%(temp['name'],temp['num'],temp['chinese'],temp['math'],temp['english']))	
while 1:
	menu()
	choose = int(input('请输入您的选择'))
	if choose == 1:
		addCard()
	elif choose == 2:
		findCard()
	elif choose == 3:
		delCard()
	elif choose == 4:
		updateCard()
	elif choose == 5:
		allCard()
	elif choose == 6:
		break
			
