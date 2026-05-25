from collections import deque


kids_names =deque(input().split())
n = int(input())

while len(kids_names) != 1:
    kids_names.rotate(-(n - 1))
    print(f"Removed {kids_names.popleft()}")
print(f"Last is {kids_names.popleft()}")