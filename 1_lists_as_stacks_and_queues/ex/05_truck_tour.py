from collections import deque

pumps_num = int(input())
pumps = deque()

for _ in range(pumps_num):
    fuel, distance = [int(x) for x in input().split()]
    pumps.append({"fuel": fuel, "distance": distance})

start_position = 0
stops = 0

while stops < pumps_num:
    curr_fuel = 0
    for i in range(pumps_num):
        curr_fuel += pumps[i]["fuel"]
        dist = pumps[i]["distance"]
        if curr_fuel < dist:
            stops = 0
            pumps.rotate(-1)
            start_position += 1
            break
        curr_fuel -= dist
        stops += 1
print(start_position)