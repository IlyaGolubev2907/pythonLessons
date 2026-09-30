from functools import reduce

tests = [
    {"name": "login", "status": "FAIL", "time": 1},
    {"name": "register", "status": "PASS", "time": 5},
    {"name": "logout", "status": "SKIP", "time": 3},
    {"name": "buy", "status": "FAIL", "time": 5},
    {"name": "checkout", "status": "PASS", "time": 4},
]

def is_failed(tests):
   return tests["status"] == "FAIL"

def get_failed_name(tests):
    return tests["name"]

def is_passed(tests):
    return tests["status"] == "PASS"

def tests_time(time, tests):
    return time + tests["time"]


failed = list(filter(is_failed, tests))
failed_names = list(map(get_failed_name, failed))
passed = [test["name"] for test in tests if is_passed(test)]
time = reduce(tests_time, tests, 0)
status_count = {
    "PASS": len([test for test in tests if is_passed(test)]),
    "FAIL": len([test for test in tests if is_failed(test)]),
    "SKIP": len([test for test in tests if test["status"] == "SKIP"]),
}

print("Статусы тестов:")
for status, count in status_count.items():
    print(f"  {status}: {count}")

print(f"Упавшие тесты: {failed_names}")
print(f"Успешные тесты: {passed}")
print(f"Время выполнения: {time}")