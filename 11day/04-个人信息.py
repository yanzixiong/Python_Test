id_card = {"name":"闫子雄","age":"21","height":"175","group":"汉"}
id_card["address"]="山西吕梁"#增
id_card["sex"]="男"
id_card.pop("group")#删
id_card["name"]="大雄"#改
print(id_card["age"])
#print(id_card["merry"])#没有这个键会报错
print(id_card.get("merry"))#没有这个键不会报错
print(id_card)
print(id_card.keys())
print(id_card.values())

