lines = []
while True:
    line = input("Enter a line (or press Enter to stop): ")
    if not line:
        break
    lines.append(line.upper())
for line in lines:
    print(line)
