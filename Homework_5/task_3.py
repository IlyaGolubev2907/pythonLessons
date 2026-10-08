def tests(attempts, timeout):
    if attempts not in range(0, 5):
        raise ValueError("Количество повторных запусков должно быть от 0 до 5")

    if timeout <= 0:
        raise ValueError("Таймаут должен быть положительным числом")

    print(f"Корректные параметры: {attempts}, {timeout}")


test_cases = [(4, 6), (4, -5), (7, 6)]

for attempts, timeout in test_cases:
    try:
        tests(attempts, timeout)
    except ValueError as e:
        print(f"Ошибка: {e}")