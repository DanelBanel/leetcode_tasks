#!/usr/bin/python3
import pytest

from tasks.task_7 import Solution


@pytest.mark.parametrize(
    "input_a, expected_output",  # Define test inputs and expected output
    [
        (123, 321),
        (-123, -321),
        (120, 21),
    ],
)
def test_7(input_a, expected_output):
    solution = Solution()
    output = solution.reverse(x=input_a)
    assert (
        output == expected_output
    ), f"Failed test for input_a: {input_a}. Got: {output}, expected: {expected_output}"
