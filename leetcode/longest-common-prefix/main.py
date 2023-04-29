class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        matchingChar = []
        
        for i in range (len(strs[0])):
            char = strs[0][i]
            for el in strs:
                if i>=len(el) or char != el[i]:
                    return "".join(matchingChar)

            matchingChar.append(char)
              
        return "".join(matchingChar)
