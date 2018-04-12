list=[]
def hero(name):
	list.append(name)
while True:
	if len(list)==5:
		print(list)
		break
	name = input ("请输入英雄名字")
	hero(name)
