rows, cols = map(int, input().split(", "))

matrix = []
sum_matrix = 0

for _ in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)
    sum_matrix += sum(row)

print(sum_matrix)
print(matrix)