children=["Петя", "Маша", "Вася", "Аня", "Слава", "Клава", "Антон", "Настя", "Наташа", "Лида", "Алина"]
print(children)
lenght=len(children)
msg_q='Всего %s детей'
print(msg_q % lenght)
i=0
boys=[]
while i<lenght:
	if i%2==0 and i!=lenght-3 and i!=lenght-1:
		print(children[i], "- мальчик")
		boys.append(children[i])
	i=i+1
msg_q1="Всего %s мальчиков: %s"
print(msg_q1 % (len(boys), boys))
