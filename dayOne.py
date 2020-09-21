class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # # first we create a dictionary
        # dictionary = {}
        # # then we loop through the numbers
        # for i in range(len(nums)):
        #      if there is a duplicate in the dictionary we return True
        #     if dictionary.get(nums[i]) is not None:
        #         return True
        #         else if there isnt we assign it to a random spot in the dictionary
        #     else:
        #         dictionary [nums[i]] = 2
        # return False

        #    we create a set and call it table
        table = set()
#    we loop through nums and if the number is already in the table we return true
        for num in nums:
            if num in table:
                return True
#             else we added the number using the .add method to add the number to the table
            else:
                table.add(num)
        return False
