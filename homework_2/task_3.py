for user in range(1, 21):
    if user in (5, 10, 15):
        continue
    print("Пользователь: ", user)
    if user == 18:
        break