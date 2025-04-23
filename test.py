from run import check_capacity


def test_from_task_1():
    result = check_capacity(2, [
        {"name": "1", "check-in": "2021-01-10", "check-out": "2021-01-15"},
        {"name": "2", "check-in": "2021-01-12", "check-out": "2021-01-20"},
        {"name": "3", "check-in": "2021-01-15", "check-out": "2021-01-21"}
    ])

    assert result == True


def test_from_task_2():
    result = check_capacity(2, [
        {"name": "1", "check-in": "2021-01-10", "check-out": "2021-01-16"},
        {"name": "2", "check-in": "2021-01-12", "check-out": "2021-01-20"},
        {"name": "3", "check-in": "2021-01-15", "check-out": "2021-01-21"}
    ])

    assert result == False


def test_few_in_row():
    result = check_capacity(5, [
        {"name": "1", "check-in": "2021-01-10", "check-out": "2021-01-12"},
        {"name": "2", "check-in": "2021-01-12", "check-out": "2021-01-14"},
        {"name": "3", "check-in": "2021-01-14", "check-out": "2021-01-16"}
    ])

    assert result == True


def test_many_in_row():
    result = check_capacity(2, [
        {"name": "1", "check-in": "2021-01-10", "check-out": "2021-01-12"},
        {"name": "2", "check-in": "2021-01-12", "check-out": "2021-01-14"},
        {"name": "3", "check-in": "2021-01-14", "check-out": "2021-01-16"}
    ])

    assert result == True


def test_exact_in_row():
    result = check_capacity(3, [
        {"name": "1", "check-in": "2021-01-10", "check-out": "2021-01-12"},
        {"name": "2", "check-in": "2021-01-12", "check-out": "2021-01-14"},
        {"name": "3", "check-in": "2021-01-14", "check-out": "2021-01-16"}
    ])

    assert result == True
