import random
i = 1
j = int(input("请输入次数"))
while i <= j:
	computer = random.randint(1,3)

	player = int(input("请输入1---石头 2---剪刀 3---布"))

	if (player ==1 and computer ==2) or (player ==2 and computer ==3) or (player ==3 or computer ==1):
		print("玩家赢")
	else:
		print("电脑赢")
	i+=1
