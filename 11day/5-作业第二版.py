list = []
dd = []
dict = {}
name = input('请输入姓名')
sex  = input('请输入性别')
qq = input('请输入qq号码')
age = int(input('请输入年龄'))
weight =float(input("请输入体重"))
age1 = 0
age1 += age
dict['姓名'] = name
dict['性别'] = sex
dict['年龄'] = age
dict['qq'] = qq
dict['体重'] = weight
list.append(dict)
dd.append(dict['姓名'])
print('*'*20)
for i in range(0,2):
    dict = {}
    name = input('请输入姓名')
    sex  = input('请输入性别')
    qq = input('请输入qq号码')
	weight =float(input("请输入体重"))
    age = int(input('请输入年龄'))
    print('*' * 20)
    if name in dd:
        print('名字重复，请重新输入')
    else:
        dict['姓名'] = name
        dict['性别'] = sex
        dict['qq'] = qq
        dict['年龄'] = age
		dict['体重'] = weight
        list.append(dict)
        dd.append(dict['姓名'])
        age1 += age
print('------------------------------------------')
print('------------------------------------------')
print('------------------------------------------')
print('------------------------------------------')
print('------------------------------------------')
print('------------------------------------------')
for a in list:
    #print(a)
    for k,v in a.items():
        print('%s:%s'%(k,v))
    print('*' * 20)
print('平均年龄为%0.2f'%(age1/len(list)))


