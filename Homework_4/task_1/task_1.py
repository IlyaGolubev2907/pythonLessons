with open("numbers.txt", "r") as f:
    numbers = []

    for line in f:
        for num in line.split():
            numbers.append(int(num.strip(",")))

if len(numbers) < 3:
    print("В файле меньше 3 чисел")
else:
    print("Первый элемент:", numbers[0])
    print("Второй элемент:", numbers[1])
    print("Предпоследний элемент:", numbers[-2])
    print("Последний элемент:", numbers[-1])