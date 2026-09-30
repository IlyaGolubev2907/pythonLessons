import random

tests = [
    "test_login",
    "test_logout",
    "test_registration",
    "test_profile",
    "test_payment",
    "test_search"
]

results = ["PASS", "FAIL", "SKIP"]

tests_count = int(input("Введите количество тестов: "))
if tests_count > len(tests):
    print("Тестов больше, чем в списке")
else:
    test_run = random.sample(tests, tests_count)

    print("Отчёт о запуске тестов: ")

    for test in test_run:
        result = random.choice(results)
        print(f"{test}: {result}")

