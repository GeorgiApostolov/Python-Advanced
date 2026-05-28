rows = int(input())

matrix = []
final_matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

for i in range(len(matrix)):
    current_row = []
    for j in range(len(matrix[i])):
        current_element = matrix[i][j]
        if current_element % 2 == 0:
            current_row.append(matrix[i][j])

    final_matrix.append(current_row)

print(final_matrix)
