#!/usr/bin/python3


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        for idx in range(len(x_str) // 2):
            front_elt = x_str[idx]
            back_elt = x_str[-(idx + 1)]
            if front_elt != back_elt:
                return False
        return True
