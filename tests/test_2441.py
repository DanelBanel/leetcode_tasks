#!/usr/bin/python3
import pytest

from tasks.task_2441 import Solution


@pytest.mark.parametrize(
    "input_a, expected_output",  # Define test inputs and expected output
    [
        ([-1, 2, -3, 3], 3),
        ([-1, 10, 6, 7, -7, 1], 7),
        ([-10, 8, 6, 7, -2, -3], -1),
    ],
)
def test_2942(input_a, expected_output):
    solution = Solution()
    output = solution.findMaxK(nums=input_a)
    assert (
        output == expected_output
    ), f"Failed test for input_a: {input_a}. Got: {output}, expected: {expected_output}"
