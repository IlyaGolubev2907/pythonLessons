class InvalidTestStatusError(Exception):
    pass


def check_test_status(status):
    if status not in ("PASS", "FAIL", "SKIP"):
        raise InvalidTestStatusError(f"Некорректный статус: {status}")

    print(f"Статус: {status}")


test_status = ["PASS", "FAIL", "SKIP", "ERROR", "UNKNOWN"]

for status in test_status:
    try:
        check_test_status(status)
    except InvalidTestStatusError as e:
        print(f"Ошибка: {e}")
