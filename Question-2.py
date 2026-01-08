data = []

print("Enter tuples (press Enter on empty line to stop):")

while True:
    line = input()
    if line == "":
        break
    name, age, height = line.split(",")
    data.append((name, age, height))

result = sorted(data, key=lambda x: (x[0], int(x[1]), int(x[2])))

print(result)
