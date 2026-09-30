with open("numbers.txt", "r") as f1, open("numbers2.txt", "r") as f2:
    swap1 = f1.read()
    swap2 = f2.read()

with open("numbers.txt", "w") as f1, open("numbers2.txt", "w") as f2:
    f1.write(swap2)
    f2.write(swap1)