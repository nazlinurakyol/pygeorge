class Solution:
    def isPalindrome(self, x: int) -> bool:
        numStr = str(x)
        for i in range(0, len(numStr)):
            if numStr[i] != numStr[len(numStr) -1 - i] :
                return False
        
        return True