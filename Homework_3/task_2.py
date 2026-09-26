test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]


def print_report(test_cases, statuses):
    result = zip(test_cases, statuses)
    passed = 0
    failed = 0
    skipped = 0

    for test, status in result:
        print(f"{test} - {status}")

        if status == "PASS":
            passed += 1
        elif status == "FAIL":
            failed += 1
        elif status == "SKIP":
            skipped += 1

    print(f"PASS: {passed}, FAIL: {failed}, SKIP: {skipped}")

    if failed == 0:
        print("Запуск успешный")
    else:
        print("Запуск неуспешный")


print_report(test_cases, statuses)
