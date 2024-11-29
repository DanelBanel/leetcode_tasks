#!/usr/bin/python3
import pytest

from tasks.task_2942 import Solution


@pytest.mark.parametrize(
    "input_a, input_b, expected_output",  # Define test inputs and expected output
    [
        (["leet", "code"], "e", [0, 1]),
        (["abc", "bcd", "aaaa", "cbc"], "a", [0, 2]),
        (["abc", "bcd", "aaaa", "cbc"], "z", []),
    ],
)
def test_2942(input_a, input_b, expected_output):
    solution = Solution()
    output = solution.findWordsContaining(words=input_a, x=input_b)
    assert (
        output == expected_output
    ), f"Failed test for input_a: {input_a}, input_b: {input_b}. Got: {output}, expected: {expected_output}"
