cars = []
car = []
def menu():
	print("大众4S店购车系统")
	print("1:录入汽车信息".center(30,"*"))
	print("2:查询车辆信息".center(30,"*"))
	print("3:修改汽车信息".center(30,"*"))
	print("4:删除汽车信息".center(30,"*"))
	print("5:显示所有车辆信息".center(30,"*"))
	print("6:售后服务".center(30,"*"))
	print("7:退出系统".center(30,"*"))

def addcar():
	dic = {}
	name = input("请输入汽车名字")
	price = int(input("请输入汽车价格"))
	model = input("请输入汽车型号")
	if model in car:
		for temp in cars:
			if model == temp['model']:
				queren()
	#queren()			
	color = input("请输入汽车颜色")
	home = input("请输入汽车厂家")
	dic['name'] = name
	dic['price'] = price
	dic['model'] = model
	dic['color'] = color
	dic['home'] = home
	cars.append(dic)
	car.append(model)
	print("添加成功")

def queren():
	#if model in car:
		#for temp in cars:
			#if model == temp['model']:
	while 1:		
		queren = int(input("该型号的车已经存在,是否继续添加1:是 2:否"))
		if queren ==1:
			addcar()
		else:
			break

def findcar():
	types = int(input("您要根据哪一项吗目进行查询1:车名2:车型3:价格4:颜色5:厂家"))
	if types == 1:
		a_name = input("请输入要查找的车名")
		if a_name in cars:
			print("d")
	elif types ==2:
		a_model = input("请输入要查找的车型")

	elif types ==3:
		a_price = input("请输入要查找的车价")

	elif types ==4:
		a_color = input("请输入要查找的汽车颜色")

	elif types ==5:
		a_home = input("请输入要查找的车辆厂家")
	else:
		print("对不起，没有您要查询的项目")

				
					


def updatecar():
	#model = input("输入要修改的汽车型号")
	#if model in car:
	types = int(input("请输入要修改的类型:1.车名 2价格 3型号 4颜色 5厂家"))
		
	for temp in cars:
		if types == 1:
			new_name = input("请输入新的车名")
			temp['name'] = new_name
		elif types == 2:
			new_price = int(input("请输入新的价钱"))
			temp['price'] = new_price
		elif types == 3:
			new_model = input("请输入新的车型")
			temp['model'] = new_model
		elif types == 4:
			new_color = input("请输入新颜色")
			temp['color'] = new_color
		elif types == 5:
			new_home = input("请输入新的厂家")
			temp['home'] = new_home
			print("修改成功")
		else:
			print("修改失败")


def delcar():
	a_type = int(input("请输入要删除的项目1:车型2:车名3:车价4:颜色5:厂家"))
	if a_type ==1:
		models = input("请输入要删除的汽车型号")
		if models in car:
			for temp in cars:
				if models == temp['model']:
					cars.remove(temp)
					car.remove(models)
					print("删除成功")
				else:
					continue
		else:
			print("汽车型号输入错误")
	elif a_type ==2:
		s_name = input("请输入要删除的汽车名字")
		if s_name in car:
			for temp in cars:
				if s_name == temp['name']:
					cars.remove(temp)
					car.remove(s_name)
					print("删除成功")
				else:
					continue
		else:
			print("汽车名字输入错误")
	elif a_type ==3:
		s_price = input("请输入要删除的汽车价格")
		if s_price in car:
			for temp in cars:
				if s_price== temp['price']:
					cars.remove(temp)
					car.remove(s_price)
					print("删除成功")
				else:
					continue
		else:
			print("汽车价格输入错误")
	elif a_type ==4:
		s_color = input("请输入要删除的汽车颜色")
		if s_color in car:
			for temp in cars:
				if s_color == temp['color']:
					cars.remove(temp)
					car.remove(s_color)
					print("删除成功")
				else:
					continue
		else:
			print("汽车颜色输入错误")
	elif a_type ==5:
		s_home = input("请输入要删除的汽车厂家")
		if s_home in car:
			for temp in cars:
				if s_home == temp['home']:
					cars.remove(temp)
					car.remove(s_home)
					print("删除成功")
				else:
					continue
		else:
			print("汽车厂家输入错误")
	else:
		print("您要删除的项目有误")


def sellcar():
	print("首先祝贺您购到心爱的车，我店里为了答谢新老顾客，推出一系列优惠活动")
	sellprice = int(input("请选择您的价位1:5万-8万 2:8万-12万 3:12万-20万 4:20万以上"))
	if sellprice ==1:
		print("优惠2000元")
	elif sellprice ==2:
		print("免费保养一次+200元加油卡")
	elif sellprice ==3:
		print("液晶电视一台")
	elif sellprice == 4:
		print("iphone8Plus一部")
	else:
		print("200元加油卡")


def allcar():
	for temp in cars:
			print("车名%s\n价钱%d\n车型%s\n颜色%s\n厂家%s\n"%(temp['name'],temp['price'],temp['model'],temp['color'],temp['home']))


while True:
	menu()
	choose = int(input("请输入您的选择"))
	if choose == 1:
		addcar()
		#queren()
	elif choose == 2:
		findcar()
	elif choose == 3:
		updatecar()
	elif choose == 4:
		delcar()
	elif choose ==5:
		allcar()
	elif choose ==6:
		sellcar()
	elif choose ==7:
		break
		
