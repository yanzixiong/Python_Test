import time
def playgame():
	for i in range(10):
		print("正在吃鸡，哒哒哒")
		time.sleep(1)
	print("你爸爸来了")
	result = kill()
	if result == "削惨了":
		print("game over")
	else:
		print("go on")
def kill():
	print("一顿削")
	say()
	return "削惨了"
def say():
	print("就知道打游戏")
playgame()
