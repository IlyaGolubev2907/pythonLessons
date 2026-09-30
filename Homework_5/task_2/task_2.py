import json

try:
    with open("test_data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError as e:
    print(f"Файл не найден: {e}")
except json.JSONDecodeError as e:
    print(f"Не удалось прочитать JSON: {e}")
else:
    users = data["users"]

    for user in users:
        try:
            login = user["login"]
            password = user["password"]
            expected_result = user["expected_result"]
            print(f"Логин: {login}, Пароль: {password}, Результат: {expected_result}")
        except KeyError as e:
            print(f"Отсутствует обязательное поле: {e}")

