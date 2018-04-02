year = float(input("请输入年份"))
if (year %4 ==0 and year%4 != 0) or year %400 == 0:
	print("闰年")
else:
	print("平年")
