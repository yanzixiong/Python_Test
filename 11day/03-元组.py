a = ("xiaowang","xiaoming","xiaoli")
b = input("请输入一个名字")
if b in a:
	print("xiaowangzai")
else:
	print("buzai")
	


if b not in list(a):
	print("buzai")
else:
	print("zai")

