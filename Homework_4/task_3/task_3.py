with open("numbers.txt", "r") as f:
    numbers = []
    for line in f:
        for num in line.split():
            numbers.append(float(num))

with open("numbers.txt", "w") as f:
    for num in numbers:
        f.write(str(num ** 2) + " ")