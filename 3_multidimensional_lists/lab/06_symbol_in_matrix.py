n = int(input())

matrix = []

for _ in range(n):
    current_row = list(input())
    matrix.append(current_row)

find_symbol = input()
index = list()
is_find = False

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if find_symbol == matrix[row][col]:
            index.append(row)
            index.append(col)
            is_find = True
            print(f"({row}, {col})")
            exit()

print(f"{find_symbol} does not occur in the matrix")
