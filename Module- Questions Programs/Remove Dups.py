input_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
seen = set()
output_list = []
for item in input_list:
    if item not in seen:
        output_list.append(item)
        seen.add(item)
print(output_list)