letter = input("Please, enter the letter: ")
letter_index = ord(letter)

print('Entered symbol: ', letter)

if letter.lower() != 'a':
    prev_letter = chr(letter_index - 1)
    print('Prev symbol: ', prev_letter)

if letter.lower() != 'z':
    next_letter = chr(letter_index + 1)
    print('Next symbol: ', next_letter)