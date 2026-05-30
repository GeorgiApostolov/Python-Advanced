rows, cols = map(int, input().split(", "))

matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split(" "))))

for col in range(cols):
    current_sum = 0
    for row in range(rows):
        current_el = matrix[row][col]
        current_sum += current_el
    print(current_sum)