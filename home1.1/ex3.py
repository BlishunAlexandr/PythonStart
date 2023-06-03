# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Максимальное число: "))
start = 2
stepen = 1

while start <= N:
    print(f"2^{stepen}={start} ")
    start *= 2
    stepen += 1