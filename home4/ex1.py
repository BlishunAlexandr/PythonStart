letters = ['А', 'О', 'У', 'Э', 'Ы', 'Я', 'Ё', 'Е', 'Ю', 'И']
poem = input("стих: ").split()
print(poem)
variable = list()
trigger = False
for i in poem:
    counter = 0
    for j in i:
        if j.upper() in letters:
            counter += 1
    variable.append(counter)
for i in variable:
    for j in variable:
        if i != j:
            trigger = True
            break
    if trigger == True:
        print("Пам парам")
        break

if trigger == False:
    print("Парам пам-пам")