
num = input('введіть ціле число: ')  

def sum_digits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)
    
print('число: {}'.format(num))
print('сума цифр: {}'.format(sum_digits(num)))
print('кількість цифр: {}'.format(len(num)))
