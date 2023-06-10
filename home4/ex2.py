def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        spisok = list(map(lambda x: operation(row, x), range(1, num_columns + 1)))
        print(*spisok)

print_operation_table(lambda x, y: x * y)