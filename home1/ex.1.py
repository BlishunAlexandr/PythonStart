# Найдите сумму цифр трехзначного числа.
num = int(input("Трехзначное число: "))
if num >= 100 and num <= 999:
    i = 0
    total = 0
    while i < 3:
        total = total + num % 10
        num = num // 10
        i += 1
    print(total)
else:
    print("нужно трехзначное число")