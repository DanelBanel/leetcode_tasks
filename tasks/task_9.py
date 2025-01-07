class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        for idx in range(len(x_str) // 2):
            front_elt = x_str[idx]
            back_elt = x_str[- (idx+1)]
            #print(f"Index: {idx}")
            #print(f"Value front: {front_elt}")
            #print(f"Value back: {back_elt}")
            if front_elt != back_elt:
                return False
        return True