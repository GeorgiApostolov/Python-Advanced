from collections import deque


liters_water = int(input())
people = deque()
input_string = input()
while input_string != "Start":
    people.append(input_string)
    input_string = input()
input_string = input()
while input_string != "End":
    if input_string.split()[0] == "refill":
        liters_water += int(input_string.split()[1])
    elif int(input_string) > liters_water:
        people.popleft()
    else:
        liters_water -= int(input_string)
        print(f"{people.popleft()} got water")
    input_string = input()
if people:
    for person in people:
        print(f"{person} must wait")
print(f"{liters_water} liters left")