def is_valid_coordinates(row1, col1, row2, col2, rows, cols):
    return row1 >= 0 and row1 < rows and col1 >= 0 and col1 < cols and row2 >= 0 and row2 < rows and col2 >= 0 and col2 < cols

r, c = map(int, input().split())
matrix = [input().split() for _ in range(r)]

while True:
    line = input()
    if line == "END":
        break
    command = line.split()
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue

    r1, c1, r2, c2 = map(int, command[1:])
    if is_valid_coordinates(r1, c1, r2, c2, r, c):
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        [print(*row) for row in matrix]
    else:
        print("Invalid input!")