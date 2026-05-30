n = int(input())

matrix = []
final_list = []

for _ in range(n):
    matrix.append(list(map(int, input().split(" "))))

for i in range(n):
    current_el = matrix[i][i]
    final_list.append(current_el)
print(sum(final_list))