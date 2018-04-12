list = [{"beijing":{"mianji":1290,"remkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]
def information():
	for i in list:
		for k,v in i.items():
			for j,l in v.items():
				print(k,j,l)			
information()
