import pytest
import sample_module


def test_sort_numbers():
    numbers = [-10, -1, 5, 9, 10]
    actual = sample_module.sort_numbers(numbers)
    expected = [-10, 10, 5, 9, -1] # if we don't know the excepted then put empty list expected = [] then the output error will say the answer

    assert actual == expected


def test_reverse_numbers():
    numbers = [5, 9, -1, -10, 10]
    actual = sample_module.reverse_numbers(numbers)
    expected = [10, -1,  9, -10, 5]

    assert actual == expected

