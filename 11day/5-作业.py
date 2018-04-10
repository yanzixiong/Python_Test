list = []
dd = []
i = 0
while i <=2:
	dict = {}
	a_name = input("请输入姓名")	
	a_age =int(input("请输入年龄"))
	a_sex = input("请输入性别")
	a_qqnumber = input("请输入QQ号")
	a_weight =float(input("请输入体重"))
	if a_name not in dd:

		dict['name']=a_name
		dict['age']=a_age
		dict['sex']=a_sex
		dict['qqnumber']=a_qqnumber
		dict['weight']=a_weight
		list.append(dict)
		dd.append(dict['name'])
		print(list)
		i+=1
	else:
		print('名字重复')
age1 = 0
print("*"*50)
for i in list:
	age1=+i.get('age')
	print(i)
print('平均年龄是%0.2f'%(age1/3))
print("*"*50)

