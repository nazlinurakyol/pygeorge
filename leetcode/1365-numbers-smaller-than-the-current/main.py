class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        count = 0
        for el in nums:
            for i in range(0, len(nums)):
                if el > nums[i]:
                    count += 1
            answer.append(count)
            count = 0
        return answer
