class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        
        while(len(s)> 0) :
            if s.__contains__("IV"):
                count +=4
                s = s.replace("IV", "", 1)

            elif s.__contains__("XC"):
                count += 90
                s = s.replace("XC", "", 1)

            elif s.__contains__("CM"):
                count += 900
                s = s.replace("CM", "", 1)

            elif s.__contains__("IX"):
                count += 9
                s = s.replace("IX", "", 1)

            elif s.__contains__("XL"):
                count += 40
                s = s.replace("XL", "", 1)

            elif s.__contains__("CD"):
                count += 400
                s = s.replace("CD", "", 1)

            elif s.__contains__("M"):
                count += 1000
                s = s.replace("M", "", 1)

            elif s.__contains__("D"):
                count += 500
                s = s.replace("D", "", 1)

            elif s.__contains__("C"):
                count += 100
                s = s.replace("C", "", 1)

            elif s.__contains__("L"):
                count += 50
                s = s.replace("L", "", 1)

            elif s.__contains__("X"):
                count += 10
                s = s.replace("X", "", 1)

            elif s.__contains__("V"):
                count += 5
                s = s.replace("V", "", 1)

            elif s.__contains__("III"):
                count += 3
                s = s.replace("III", "", 1)

            elif s.__contains__("I"):
                count += 1
                s = s.replace("I", "", 1)
        
        
        return count