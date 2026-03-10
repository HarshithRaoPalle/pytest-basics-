def test_variables():
    username = "admin"
    password = "1234"

    assert username == "admin"
    assert password == "1234"


def test_list_example():
    browsers = ["chrome", "firefox", "edge"]

    assert "chrome" in browsers
    assert len(browsers) == 3


def test_loop_example():
    numbers = [1, 2, 3, 4]

    total = 0

    for num in numbers:
        total = total + num

    assert total == 10