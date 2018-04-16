def zhuce(phone,pwd):
	result = isphone(phone)
	if result:
		print("注册成功")
	else:
		print("注册失败")

def login(phone,pwd):
	result = isphone(phone)
	if result:
		print("登录成功")
	else:
		print("登录失败")


def isphone(phone):
	if phone.startswith("1") and len(phone)==11:
		return True
	else:
		return False

zhuce("12345678987","123456")

login("15135241451","123456")
