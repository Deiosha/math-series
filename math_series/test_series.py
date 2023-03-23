from series import fibonacci
from series import lucas
from series import sum_series


def test_fibonacci1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci2():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected


def test_fibonacci3():
    actual = fibonacci(13)
    expected = 233
    assert actual == expected


def test_lucas1():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas2():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas3():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_sum_series1():
    actual = sum_series(5, 2, 1)
    expected = 11
    assert actual == expected


def test_sum_series2():
    actual = sum_series(6, 6, 1)
    expected = 38
    assert actual == expected


def test_sum_series3():
    actual = sum_series(5, 13, 6)
    expected = 69
    assert actual == expected