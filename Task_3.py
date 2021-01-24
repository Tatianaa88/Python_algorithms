# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

import string

let1 = input('Please enter your 1st letter: ')
let2 = input('Please enter your 2nd letter: ')

symbols = string.ascii_letters
symb1_ind = (symbols.find(let1) + 1)
symb2_ind = (symbols.find(let2) + 1)

if symb1_ind < symb2_ind:
    delta = (symb2_ind - symb1_ind) - 1
else:
    delta = (symb1_ind - symb2_ind) - 1

print(symb1_ind)
print(symb2_ind)
print(delta)
