def get_input_data(message):
    while True:
        try:
            value = input(message)
            return float(value)
        except:
            print('Введіть числове значення')

price_per_kg = get_input_data('Введіть ціну за кг: ')
price_per_gramm = price_per_kg / 1000

for piece_weight in range(50, 1050, 50):
     piece_price = price_per_gramm * piece_weight
     print('кількість в грамах: {} ціна: {}'.format(piece_weight, piece_price))
