children={
	{
	"name":"Петя",
	"gender": "m"
	},
	{"name":"Маша",
	"gender":"f"
	},
	{"name": "Вася",
	"gender":"m"
	},
	{"name": "Аня",
	"gender":"f"
	},
	{"name": "Слава",
	"gender":"m"
	},
	{"name": "Клава",
	"gender":"f"
	},
	{"name": "Антон",
	"gender":"m"
	},
	{"name": "Настя",
	"gender":"f"
	},
	{"name": "Наташа",
	"gender":"f"
	},
	{"name": "Лида",
	"gender":"f"
	},
	{"name": "Алина",
	"gender":"f"
	}
}
print(children)
lenght=len(children)
msg_q='Всего %s детей'
print(msg_q % lenght)
i=0
for i in children:
	if i%2==0 and i!=lenght-3 or i!=lenght-1:
		print(children[i], "- мальчик")
	i=i+1

