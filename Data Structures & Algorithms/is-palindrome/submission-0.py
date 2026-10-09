class Solution:
    def isPalindrome(self, s: str) -> bool:
        # text that joing lower case alphanumeric chars. '' means no space in the join
        text = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(text) - 1

        while left < right:
            if text[left] == text[right]:
                left +=1
                right -=1
            else:
                return False
        return True

        # Space O(n)
        # Time O(n)