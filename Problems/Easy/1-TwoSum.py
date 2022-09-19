class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for count, value1 in enumerate(nums):
            value2 = target - value1
            if value2 in dictionary:
                return [count, dictionary[value2]]
            else:
                dictionary[value1] = count

lista = [3,2,4]
target = 6


