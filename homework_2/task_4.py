secret_number = 37
count = 0

while True:
    attempt = int(input("Введите число: "))
    count += 1

    if attempt == secret_number:
        print("Введено верное число, количество попыток: ", count)
        break
    elif attempt < secret_number:
        print("Число меньше")
    elif attempt > secret_number:
        print("Число больше")