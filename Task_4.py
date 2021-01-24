# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string


user_letter = int(input("Please enter any letter's  sequence number: "))

symbols = string.ascii_letters
let = symbols[user_letter - 1]

print(let)
