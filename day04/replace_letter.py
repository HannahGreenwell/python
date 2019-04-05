# Method 1: create an empty output string and add characters to it

input_string = 'It is free to feed the geese.'
output_string = ''

for each_char in input_string:
    # print(each_char)
    # check if the current letter is 'e'
    # if each_char == 'e' or each_char == 'i' or each_char == 'o':
    if each_char in 'aeiou':
        output_string += '_'
    else:
        output_string += each_char

print('output_string =', output_string)

# Method 2: Convert the string into a list and replace the individual characters in place

input_string = 'It is free to feed the geese.'
string_as_list = list(input_string)

for index, char in enumerate(string_as_list):
    if char == 'e':
        string_as_list[index] = '_'

output_string = ''.join(string_as_list)
print('output_string =', output_string)
