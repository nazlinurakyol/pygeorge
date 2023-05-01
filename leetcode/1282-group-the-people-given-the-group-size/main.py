class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """

        newArr = []
        subArr = []
        used = set()

        for i in groupSizes:
            for j in range(len(groupSizes)):
                if i == groupSizes[j] and len(subArr) <= i:
                    if j not in used:
                        used.add(j)
                        subArr.append(j)
                        if len(subArr) == i:
                            newArr.append(subArr)
                            subArr = []

        return newArr
