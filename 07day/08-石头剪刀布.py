computer = 1

player = int(input("请输入1---石头 2---剪刀 3---布"))


if (player ==1 and computer ==2) or (player ==2 and computer ==1) or (player ==3 and computer ==1):
	print("玩家赢")
else:
	print("电脑赢")
