print("我找到一个更大的餐桌")
names = ["郝晨然","张碧辉","高斐","马笑海","李卓君","吕岩","王港"]
names.insert(0,"法海")
names.insert(5,"唐僧")
names.append("白娘子")
print(names)
for i in names:
	print("邀请%s跟我一起共进晚餐"%i)

print("我很抱歉，餐桌无法按时送到，我只能邀请两位嘉宾。")
name1 = names.pop()
print(name1,"我很抱歉不能与你共进晚餐")
name2 = names.pop()
print(name2,"我很抱歉不能与你共进晚餐")
name3 = names.pop()
print(name3,'我很抱歉不能与你共进晚餐')
name4 = names.pop()
print(name4,'我很抱歉不能与你共进晚餐')
name5 = names.pop()
print(name5,'我很抱歉不能与你共进晚餐')
name6 = names.pop()
print(name6,'我很抱歉不能与你共进晚餐')
name7 = names.pop()
print(name7,'我很抱歉不能与你共进晚餐')
name8 = names.pop()
print(name8,'我很抱歉不能与你共进晚餐')
print(names)
for i in names:
	print('%s你依然在受邀人之列'%i)
del names[0:2]
print(names)

