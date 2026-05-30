num_of_matrix_rows = int(input())

matrix = []

for i in range(num_of_matrix_rows):
    current_row = list(int(x) for x in input().strip().split(", "))
    matrix.extend(current_row)

print(matrix)