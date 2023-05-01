class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        C = []
        for i in range(0, n):
            C.append(nums[i])
            C.append(nums[n+i])
        
        return C