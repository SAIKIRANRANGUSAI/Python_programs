import pytest


def add_two_numbers(a: float, b: float) -> float:
    for num in [a, b]:
        if not isinstance(num, float | int):
            return 0
    return a + b


class testgroup:
    def one_plus_one_is_two(self):
        a, b = 1, 1
        actual = add_two_numbers(a, b)
        expected = 0
        assert actual == expected

    def hi(self):
        a, b = 1, 'z'
        actual = add_two_numbers(a, b)
        expected = 0

        assert actual == expected

