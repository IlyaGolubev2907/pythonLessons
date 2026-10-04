def count_passed(tests):
    if not tests:
        return 0

    if tests[0] == "PASS":
        return 1 + count_passed(tests[1:])
    else:
        return count_passed(tests[1:])


tests = ["PASS", "FAIL", "PASS", "SKIP", "PASS", "FAIL", "PASS", "FAIL", "PASS", "SKIP", "PASS", "FAIL"]

print(count_passed(tests))