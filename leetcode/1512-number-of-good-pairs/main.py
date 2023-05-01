class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            for j in range (1, len(nums)):
                if i == nums[j] and nums.index(i) < j :
                    count +=1

        return count/2
