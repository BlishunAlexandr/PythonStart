# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def degree(A, B):
    if B == 1:
        return A
    return A * degree(A, B-1)

print(degree(2, 3))