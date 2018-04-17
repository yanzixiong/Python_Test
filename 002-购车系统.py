cars = []
car = []
def menu():
	print("大众4S店购车系统")
	print("1:录入汽车信息".center(30,"*"))
	print("2:查询车辆信息".center(30,"*"))
	print("3:修改汽车信息".center(30,"*"))
	print("4:删除汽车信息".center(30,"*"))
	print("5:显示所有车辆信息".center(30,"*"))
	print("6:退出系统".center(30,"*"))
def addcar():
	dic = {}
	name = input("请输入汽车名字")
	price = int(input("请输入汽车价格"))
	model = input("请输入汽车型号")
	color = input("请输入汽车颜色")
	home = input("请输入汽车厂家")
	if model in car:
		print("该型号汽车已经存在")
	dic['name'] = name
	dic['price'] = price
	dic['model'] = model
	dic['color'] = color
	dic['home'] = home
	cars.append(dic)
	car.append(model)
	print("添加成功")


def findcar():
	models = input("请输入要查找的车型")
	if models in car:
		for temp in cars:
			if models == temp['model']:
				print("车名%s\n价钱%d\n车型%s\n颜色%s\n厂家%s\n"%(temp['name'],temp['price'],temp['model'],temp['color'],temp['home']))
			else:
				print("输入的汽车型号有误")






def updatecar():
	model = input("输入要修改的汽车型号")
	if model in car:
		
		for temp in cars:
			types = int(input("请输入要修改的类型:1.车名 2价格 3型号 4颜色 5厂家"))
			if types == 1:
				new_name = input("请输入新的车名")
				temp['name'] = new_name
			elif types == 2:
				new_price = int(input("请输入新的价钱"))
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




def delcar():
	models = input("请输入要删除的车号")
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
		break
		
