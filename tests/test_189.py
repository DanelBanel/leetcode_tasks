#!/usr/bin/python3
import pytest

from tasks.task_189 import Solution


@pytest.mark.parametrize(
    "input_a, input_b, expected_output",  # Define test inputs and expected output
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ],
)
def test_1(input_a, input_b, expected_output):
    solution = Solution()
    output = solution.rotate(nums=input_a, k=input_b)
    assert (
        output == expected_output
    ), f"Failed test for input_a: {input_a}, input_b: {input_b}. Got: {output}, expected: {expected_output}"
