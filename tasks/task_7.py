class Solution:
    def reverse(self, x: int) -> int:
        rev_int = 0
        inverse = False
        if x < 0:
            inverse = True
            x = -x
        while x > 0:
            last_int = x % 10
            print("Last int", last_int)
            rev_int = rev_int * 10 + last_int
            if rev_int >= 2**31 - 1:
                print("TOO LARGE")
                return 0
            print("Rev: ", rev_int)

            x //= 10
            print("Remaining: ", x)


        if inverse:
            rev_int = -rev_int
        return rev_int