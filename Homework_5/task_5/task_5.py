import json

try:
    with open("tests.json", "r") as f:
        data = json.load(f)
except FileNotFoundError as e:
    print(f"Файл не найден: {e}")
except json.JSONDecodeError as e:
    print(f"Не удалось прочитать JSON: {e}")
else:
    tests = data["tests"]

    total = len(tests)
    passed = 0
    failed = 0
    skipped = 0
    total_duration = 0

    for test in tests:
        try:
            if test["status"] == "PASS":
                passed += 1
            elif test["status"] == "FAIL":
                failed += 1
            elif test["status"] == "SKIP":
                skipped += 1

            total_duration += test["duration"]

        except KeyError as e:
            print(f"Отсутствует обязательное поле: {e}")

    failed_tests = [test["name"] for test in tests if test["status"] == "FAIL"]

    longest_test = max(tests, key=lambda test: test["duration"])

    for test in tests:
        try:
            name = test["name"]
            status = test["status"]
            duration = test["duration"]

        except KeyError as e:
            print(f"Неправильная структура тестовых данных: {e}")

    report = {
        "total": total,
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "failed_tests": failed_tests,
        "longest_test": longest_test,
        "total_duration": total_duration
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)