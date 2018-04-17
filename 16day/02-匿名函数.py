fun = lambda a,b: a+b
print(fun(1,2))



def test(a,b,fun):	
	print(fun(a,b))

test(1,2,lambda a,b:a*b)



list=[{'name':'xiaoyan','age':24},{'name':'xiaowang','age':20},{'name':'xiaoli','age':23}]
list.sort(key = lambda list:list['age'])
print(list)

