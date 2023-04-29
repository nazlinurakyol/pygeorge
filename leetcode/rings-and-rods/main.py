class Solution:
    def countPoints(self, rings: str) -> int:

        count = 0
        for i in range(10):
            if rings.__contains__("B" + str(i)) and rings.__contains__("R" + str(i)) and rings.__contains__("G" + str(i)) :
                count +=1
                
        return count
       