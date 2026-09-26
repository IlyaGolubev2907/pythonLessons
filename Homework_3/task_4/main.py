from test_data import generate_user

user_count = int(input("Введите количество пользователей: "))

users = [generate_user() for user in range(user_count)]


def print_report():
    active = 0
    inactive = 0
    blocked = 0

    for status in users:
        print(f"{status}")

        if status['status'] == "ACTIVE":
            active += 1
        elif status['status'] == "INACTIVE":
            inactive += 1
        elif status['status'] == "BLOCKED":
            blocked += 1

    print("Статусы: ")
    print(f"ACTIVE: {active}")
    print(f"BLOCKED: {blocked}")
    print(f"INACTIVE: {inactive}")


print_report()
