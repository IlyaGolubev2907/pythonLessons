for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "BugTest")
    elif i % 3 == 0:
        print(i, "Bug")
    elif i % 5 == 0:
        print(i, "Test")
    else:
        print(i)