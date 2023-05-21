# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
ticket = int(input("Номер билета: "))
trigger = False
if ticket >= 100000 and ticket <= 999999:
    trigger = True
    check1 = 0
    check2 = 0
    i = 0
if trigger == True:
    while i < 3:
        check1 = check1 + ticket % 10
        ticket = ticket // 10
        i += 1
    i = 0
    while i < 3:
        check2 = check2 + ticket % 10
        ticket = ticket // 10
        i += 1
    if check1 == check2:
        print("Yes")
    else:
        print("No")
else:
    print("ошибка")