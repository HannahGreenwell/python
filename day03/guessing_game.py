# Pseudcode:

# 1. make up a secret number
secret_number = 5
# 2. keep track of the user's answer in a variable
user_guess = int(input('Guess the magic number: '))
# 3. ask the user for their guess
while user_guess != secret_number:
# 4. keep asking the user for their guess until the guess correctly
    user_guess = int(input('Wrong! Guess again: '))
# 5. print a congratulatory message
print('Nice work!')
