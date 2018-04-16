def a_phone(phone):
	if phone.startswith("1")  and len(phone)==11:
		return True
	else:
		return False
phone=input("请输入手机号")
result = a_phone(phone)
if result == False:
	print("输入手机号有误")
phone2 = input("请输入手机号")
result = a_phone(phone2)
if result == False:
	print("输入的手机号有误")
