

def get_input_data(message):
    while True:
        try:
            value = input(message)
            return float(value)
        except:
            print('Введіть числове значення ')

amount = get_input_data('Яку суму хочете внести?: ')
percent = get_input_data('Під який відсоток?: ')
years = get_input_data('На скільки років?: ')

converted_percent = percent / 100

for i in range(int(years)):
    profit = amount * converted_percent
    amount += profit
    print('рік: {} сума: {:.2f} прибуток: {:.2f}'.format(i + 1, amount , profit))

