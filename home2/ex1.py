# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
X = int(input("Число X: "))
N = int(input("Размер массива [1..N]: "))
A = [int(i+1) for i in range(N)]
count = 0
for i in A:
    if i == X:
        count += 1 
print(count)

