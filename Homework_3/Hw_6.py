friends = {
    'Гоша':'Георгій Степанович',
    'Ваня':'Іван Іванович',
    'Таня':'Тетяна Василівна',
    'Саша':'Олександр Вікторович',
    'Оля':'Ольга Іванівна'
}

name = input('Введіть ім"я: ')

if name in friends:
    print('Привіт, ' + friends[name])
else:
    print('Я з вами не знайома')