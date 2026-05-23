input_string = input()
people = []
while input_string != "End":

    if input_string == "Paid":
        for person in people:
            print(person)
        people = []
    else:
        people.append(input_string)
    input_string = input()
print(f"{len(people)} people remaining.")