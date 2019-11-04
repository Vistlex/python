print('Hi, what is your name?')
name=input()
greeting_msg='Nice to meet you, %s!'
print(greeting_msg % name)
print('How old are you?')
age=int(input())
greeting_msg2='I think, %s is an exellent age'
print(greeting_msg2 % age)
years_ago=int(input('Write your favorite number, please  '))
print('Говоришь ли ты по-русски?')
lang=(input('Ответь "да" или "нет"   '))
if lang!='да':
    print('It\'s a pity. My Russian is better than English')
else:
    time_trav_msg='Знаешь, что будет если попасть на %s лет назад, %s?'
    print(time_trav_msg % (years_ago, name))
    if age<years_ago:
        time_trav_msg2='Останется %s лет до твоего рождения'
        n=years_ago-age
        print(time_trav_msg2 % n)
    elif age>years_ago:
        time_trav_msg3='Ты сможешь встретиться с собой возраста %s лет'
        n1=age-years_ago
        print(time_trav_msg3 % n1)
    else:
        time_trav_msg2='Ты попадешь в год cвоего рождения'
        print(time_trav_msg2)
