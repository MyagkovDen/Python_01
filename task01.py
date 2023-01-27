# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трехзначное число: "))
sum = 0
if 99 < number < 1000:
    while number > 0:
        sum += number % 10
        number = number // 10
    print(f"Сумма цифр: {sum}")
else:
    print("Вы не ввели трехзначное число!")