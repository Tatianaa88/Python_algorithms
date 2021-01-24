# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

user_input = int(input('Please enter 3-digit number'))

a = user_input % 10
b = (user_input - a) / 10 % 10
c = ((user_input -a) / 10 -b) / 10

sum = a + b + c
mltp = a * b * c

print(sum)
print(mltp)