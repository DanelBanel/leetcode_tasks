#!/usr/bin/python3
import pytest

from tasks.task_9 import Solution


@pytest.mark.parametrize(
    "input_a, expected_output",  # Define test inputs and expected output
    [
        (121, True),
        (-121, False),
        (10, False),
    ],
)
def test_9(input_a, expected_output):
    solution = Solution()
    output = solution.isPalindrome(x=input_a)
    assert (
        output == expected_output
    ), f"Failed test for input_a: {input_a}. Got: {output}, expected: {expected_output}"
