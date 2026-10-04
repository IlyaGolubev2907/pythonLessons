with open("numbers.txt", "r") as f:
    numbers = []

    for line in f:
        for num in line.split():
            numbers.append(int(num))


with open("even.txt", "w") as even, open("odd.txt", "w") as odd:
    for num in numbers:
        if num % 2 == 0:
            even.write(str(num) + " ")
        else:
            odd.write(str(num) + " ")
