recipient_surname=input('Enter a recipient surname  ')
long_space=' '*13
while True:
    recipient_gender=input('Enter a recipient gender  ')
    if recipient_gender=='male' or recipient_gender=='m':
        spel='Dear Mr %s!'
        break
    elif recipient_gender=='female' or recipient_gender=='f':
        spel='Dear Mrs %s!'
        break
    else:
        print('Wrong Gender')
print(long_space*2, 'From JSC \"Three Pines\"')
print()
print()
print(long_space, spel % recipient_surname)
print('Happy New Year! We wish you the best!')
print()
print()
print(long_space,  'The \"Three Pines\" team!')
