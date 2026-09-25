correct_password = "Python123"
attempts = 3

for attempt in range(1, attempts + 1):
    password = input("Введите пароль: ")

    if password == correct_password:
        print("Пароль верный")
        break
    else:
        print("Пароль неверный")
else:
    print("Учетная запись заблокирована")