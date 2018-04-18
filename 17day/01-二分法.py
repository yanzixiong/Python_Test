list = [1,2,3,4,5,6,7,8,9,10,52,78,61]
key = 7

center = int(len(list)/2)
if key in list:
	while 1:
		if list[center] > key:
			center = center -1
		elif list[center] < key:
			center = center +1
		elif list[center] == key:
			print("要找的数字是%d索引是%d"%(key,center))
			break 
