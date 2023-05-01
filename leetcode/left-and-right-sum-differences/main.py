class Solution(object):
    def leftRigthDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answer = []
        leftSum = []
        rightSum = []
        i = 0
        sum = 0
        for i in range (i, len(nums)):
            leftSum.append(sum)
            sum += nums[i]
        
        sum = 0
        for i in range (len(nums)):
            rightSum.append(sum)
            sum += nums[len(nums)-i -1]

        rightSum.reverse()

        for i in range(len(nums)):
            answer.append(abs(leftSum[i] - rightSum[i]))
        return answer   
