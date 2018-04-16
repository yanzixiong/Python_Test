def sumday(date):
	year = int(date[0:4])
	month = int(date[4:6])
	day = int(date[6:])
	flag = 0
	if (year%4 ==0 and year%100 !=0) or year%400 ==0:
		flag =1
		big_month = [1,3,5,7,8,10,12]
		small_month = [4,6,9,11]
		for in range(1,month):
			if i in big_month:
				allday+=31
			elif i in small_month:
				allday+=30








sumday(20180603)			
