# Написать программу, которая генерирует в указанных пользователем границах: ● случайное целое число,
# ● случайное вещественное число, ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.

import random
import string


user_int1 = int(input('Please enter the desired integer as range start'))
user_int2 = int(input('Please enter the desired integer as range end'))

rand_num = random.randint(user_int1, user_int2)

print(rand_num)

user_flt1 = float(input('Please enter the desired float as range start'))
user_flt2 = float(input('Please enter the desired float as range end'))

rand_flt = random.uniform(user_flt1, user_flt2)

print(rand_flt)

user_symb1 = input('Please enter the desired symbol(a,z) as range start').lower()
user_symb2 = input('Please enter the desired symbol(a,z) as range end').lower()

symbols = string.ascii_letters
symb1 = symbols.find(user_symb1)
symb2 = symbols.find(user_symb2)
rand_ind = random.randint(symb1, symb2)
rand_symb = symbols[rand_ind]

print(rand_symb)
