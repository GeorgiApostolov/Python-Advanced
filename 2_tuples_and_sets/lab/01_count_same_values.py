input_nums = tuple([float(x) for x in input().split()])

result = {}
for num in input_nums:
    if num not in result:
        result[num] =  input_nums.count(num)
for key, value in result.items():
    print(f"{key} - {value} times")