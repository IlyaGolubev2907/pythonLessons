autotests_count = int(input("Введите количество автотестов: "))

passed = 0
failed = 0
skipped = 0

for tests in range(1, autotests_count + 1):
    test_result = input(f"Результат теста {tests}: ")

    if test_result == "PASS":
        passed += 1
    elif test_result == "FAIL":
        failed += 1
    elif test_result == "SKIP":
        skipped += 1
    else:
        print("Неизвестный статус")

print(f"PASS: {passed}")
print(f"FAIL: {failed}")
print(f"SKIP: {skipped}")

if failed > 0:
    print("Есть тесты с ошибкой")
else:
    print("Все выполненные тесты пройдены")