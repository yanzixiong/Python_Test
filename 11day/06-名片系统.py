print("名片系统v0.0版本".center(30,"*"))

print("1:新增名片".center(30," "))

print("2:查找名片".center(30," "))

print("3:修改名片".center(30," "))

print("4:删除名片".center(30," "))

cards = []#定义空列表

while True:

	fun_number = int(input("请选择功能"))

	if fun_number ==1:

		print("新增")

		flag  = 0 #默认值 0代表不在里面

		card={}#定义空字典

		name = input("请输入名字")

		for temp in cards:

			if name == temp["name"]:

				flag = 1 #在里面

				break

			#[{1},{2},{3}]

		if flag == 1:

			print("名字重复了")

			continue

		job = input("请输入职位")
		for temp in cards:
			if job in temp["job"]:
				flag = 1
				break
		if flag ==1:
			print("职位重复了")
			continue


		phone = int(input("请输入手机号"))
		for temp in cards:
			if phone in temp["phone"]:
				flag = 1
				break
		if flag ==1:
			print("手机号重复")
			continue
		company = input("请输入公司名字")
		for temp in cards:
			if company in temp["company"]:
				flag =1 
				break
		if flag ==1:
			print("公司名字输入错误")
			continue

		address = input("请输入公司地址")
		for temp in cards :
			if address in temp["address"]:
				flag = 1
				break
		if flag ==1:
			print("公司地址输入错误")
			continue

		#lis
		t = [{},{},{}]	

		#if flag == 0:

		card["name"] = name

		card["job"]  = job

		card["phone"] = phone

		card["company"] = company

		card["address"] = address

		#放到列表中

		cards.append(card)

		print("新增成功")

		print(cards)
	if fun_number == 2:

		print("查找")	
		a_name = input("请输入查找的名字")
		a_job = input("请输入查找的职位")
		a_phone = input("请输入查找的手机号")
		a_company = input("请输入查找的公司名字")
		a_address = input("请输入查找的地址")
		for i  in cards:
			for j in i:
				if a_name in j:
					print(a_name)
				if  a_job in j:
					print(a_job)
				if a_phone in j:
					print(a_pjone)
				if a_adress in j:
					print(a_adress)
				else:
					print("查找的内容不存在")
					break

	elif fun_number == 3:

		print("修改")

	elif fun_number == 4:

		print("删除")
		b_name = input("请输入要删除的名字")
		b_job = input("请输入要删除的职务")
		b_phone = input("请输入要删除的手机号")
		b_company = input("请输入要删除的公司名字")
		b_adress = input("请输入要删除的地址")
		if b_name in card['name']:
			cards.pop('b_name')
		if b_job in card['job']:
			cards.pop('b_job')
		if b_phone in card['phone']:	
			cards.pop('b_phone')
		if b_comany in card['company']:	
			cards.pop('b_comany')
		if b_adress in card['adress']:	
			cards.pop('b_adress')
		else:
			print("输入内容有误")
