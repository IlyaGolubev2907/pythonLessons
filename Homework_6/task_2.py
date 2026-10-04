def create_time_checker(max_time):
    def check_time(time):
        if time > max_time:
            return "Лимит времени превышен"
        return "Лимит не превышен"

    return check_time


test_1 = create_time_checker(2)
test_2 = create_time_checker(5)

print(test_1(1))
print(test_2(6))
