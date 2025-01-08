#!/usr/bin/python3
import pytest

from tasks.task_1 import Solution


@pytest.mark.parametrize(
    "input_a, input_b, expected_output",  # Define test inputs and expected output
    [
        ([2, 7, 11, 15], 9, [1, 0]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [1, 0]),
    ],
)
def test_1(input_a, input_b, expected_output):
    solution = Solution()
    output = solution.twoSum(nums=input_a, target=input_b)
    assert (
        sorted(output) == sorted(expected_output)
    ), f"Failed test for input_a: {input_a}, input_b: {input_b}. Got: {output}, expected: {expected_output}"
