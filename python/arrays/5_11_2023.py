#problem link : https://leetcode.com/problems/build-array-from-permutation/


def buildArray(nums: list[int]) -> list[int]:
    new_arr = [nums[index] for index in range(0,len(nums))]
    return [nums[index] for index in new_arr]

def buildArray(nums: list[int]) -> list[int]:
    return [nums[nums[idx]] for idx in range(len(nums))]

#since the values of list is used as index for new list
def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[idx] for idx in nums]

l = [0,2,1,5,3,4]

print(buildArray(l))