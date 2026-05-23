input_string = input()
open_scobe = []
for i in range(0, len(input_string)):
    curr_char = input_string[i]
    if curr_char == '(':
        open_scobe.append(i)
    if curr_char == ')':
        if len(open_scobe) > 0:
            start = open_scobe.pop()
            end = i + 1
            print(input_string[start:end])
