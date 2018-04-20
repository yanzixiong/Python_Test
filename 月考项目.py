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
		print("该车型已存在")
		choose = int(input("该车型已存在，是否继续订购1:是2:否"))
		while True:
			if choose ==1:
				model = input("请输入汽车型号")
				dic['model'] = model
				car.append(model)
				print("添加成功")
				break
			else:
				break

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


def findcar():
	#根据类型选择车辆
	types = int(input("您要根据哪一项吗目进行查询1:车名2:车型3:价格4:颜色5:厂家"))
	if types == 1:
		a_name = input("请输入要查找的车名") 
		if a_name in car:
			for temp in cars:
				if a_name == temp['name']:
					print("车名%s\n价钱%d\n车型%s\n颜色%s\n厂家%s\n"%(temp['name'],temp['price'],temp['model'],temp['color'],temp['home']))
				else:
					print("您要查找的车辆已经售出")
		else:
			print("输入的车名有误")
	elif types ==2:
		a_model = input("请输入要查找的车型")
		if a_model in car:
			for temp in cars:
				if a_model == temp['model']:
					print("车名%s\n价钱%d\n车型%s\n颜色%s\n厂家%s\n"%(temp['name'],temp['price'],temp['model'],temp['color'],temp['home']))
				else:
					print("你要查找的车辆已经售出")
		else:
			print("输入的车型有误")

	elif types ==3:
		a_price = input("请输入要查找的车价")
		if a_price in car:
			for temp in cars:
				if a_price == temp['price']:
					print("车名%s\n价钱%d\n车型%s\n颜色%s\n厂家%s\n"%(temp['name'],temp['price'],temp['model'],temp['color'],temp['home']))
				else:
					print("你要查找的车辆已经售出")
		else:
			print("输入的价格有误")


	elif types ==4:
		a_color = input("请输入要查找的汽车颜色")
		if a_color in car:
			for temp in cars:
				if a_color == temp['color']:
					print("车名%s\n价钱%d\n车型%s\n颜色%s\n厂家%s\n"%(temp['name'],temp['price'],temp['model'],temp['color'],temp['home']))
				else:
					print("你要查找的车辆已经售出")
		else:
			print("输入的颜色有误")



	elif types ==5:
		a_home = input("请输入要查找的车辆厂家")
		if a_home in car:
			for temp in cars:
				if a_home == temp['home']:
					print("车名%s\n价钱%d\n车型%s\n颜色%s\n厂家%s\n"%(temp['name'],temp['price'],temp['model'],temp['color'],temp['home']))
				else:
					print("你要查找的车辆已经售出")
		else:
			print("输入的厂家有误")
	else:
		print("对不起，没有您要查询的项目")

				
					


def updatecar():
	model = input("输入要修改的汽车型号")
	flag = 0
	for temp in cars:
		if model == temp['model']:
			flag = 1
			types = int(input("请输入要修改的类型:1.车名 2价格 3型号 4颜色 5厂家"))
		
			if types == 1:
				new_name = input("请输入新的车名")
				temp['name'] = new_name
				print("修改成功")
			elif types == 2:
				new_price = int(input("请输入新的价钱"))
				temp['price'] = new_price
				print("修改成功")
			elif types == 3:
				new_model = input("请输入新的车型")
				temp['model'] = new_model
				print("修改成功")
			elif types == 4:
				new_color = input("请输入新颜色")
				temp['color'] = new_color
				print("修改成功")
			elif types == 5:
				new_home = input("请输入新的厂家")
				temp['home'] = new_home
				print("修改成功")
			else:
				print("修改失败")

def delcar():
	model = input("请输入汽车型号")
	if model in car:
		for temp in cars:
			if model == temp['model']:
				cars.remove(temp)
				car.remove(model)
				print("删除成功")
			else:
				continue
	else:
		print("没有查询到该型号")

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
		
