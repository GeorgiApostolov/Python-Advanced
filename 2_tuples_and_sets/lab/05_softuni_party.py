n = int(input())

guests = set()

for i in range(n):
    guests.add(input())

command = input()

while command != 'END':
    guests.remove(command)
    command = input()

print(len(guests))

sorted_guests = sorted(guests)
for guest in sorted_guests:
    print(guest)