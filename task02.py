# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

S = int(input("Введите число журавликов: "))
petya = int(S/6)
serg = petya
katya = (petya + serg) * 2
print(f'Петя - {petya}, Катя - {katya}, Cережа - {serg}')