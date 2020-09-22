class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #         first we create an empty dictionary
        dic = {}
#     for each number in the list of numbers
        for i, num in enumerate(nums):
            #         we look if the result in the dictionary
            if num in dic:
                #         if found we return the index of the number and index of the dictionary lookup result
                return [dic[num], i]
# else we subtract the target value with the num and set it equal to i
            else:
                dic[target - num] = i
