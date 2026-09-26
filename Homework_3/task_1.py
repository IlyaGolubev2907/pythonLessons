def get_test_statistics():
    count = {"PASS": 0, "FAIL": 0, "SKIP": 0}
    for result in results:
        if result in count:
            count[result] += 1
    return count


results_input = input("Введите результаты тестов: ")
results = results_input.split()

count = get_test_statistics()
total = len(results)
successful_tests = (count['PASS'] / total * 100)

print(f"Всего тестов: {len(results)}")
print(f"PASS: {count['PASS']}")
print(f"FAIL: {count['FAIL']}")
print(f"SKIP: {count['SKIP']}")
print(f"Успешно: {successful_tests:.1f}%")