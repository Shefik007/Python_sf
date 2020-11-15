def get_input_data(message):
    while True:
        try:
            value = input(message)
            return int(value)
        except:
            print('Введіть числове значення ')

begin_interval = get_input_data('Введіть початкове значення: ')
end_interval = get_input_data('Введіть кінцеве значення: ')

if begin_interval > end_interval:
    print('початкове значення має бути меншим за кінцеве')

numbers = range(begin_interval, end_interval)

result = list(filter(lambda x: not x % 2, numbers))
print ('парні: {}'.format(result))

result2 = list(filter(lambda x: x % 2, numbers))
print ('непарні: {}'.format(result2))
