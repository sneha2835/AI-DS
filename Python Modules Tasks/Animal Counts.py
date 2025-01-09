di = [
    {"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49},
    {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7},
    {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89},
    {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}
]

total_puppies = 0

for d in di:
    try:
        total_puppies += d["Puppies"]
    except KeyError:
        continue

print(f"Total number of puppies: {total_puppies}")
