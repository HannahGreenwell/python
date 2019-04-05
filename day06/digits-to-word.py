input_string = '123'

def digits_to_word(str):

    digits_lookup = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
    }

    output = ''

    for char in str:
        output += digits_lookup[char] + ' '
        # Prints all variables
        # print(vars())

    return output

print('input:', input_string)
print('output:', digits_to_word(input_string))
