
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(i != j):
                if(nums[i] + nums[j] == target):
                    print(str(i)+" "+str(j))
                    return [i,j]


print(twoSum(([2,7,11,15]),9))

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i != j):
                    if(nums[i] + nums[j] == target):
                        break;
                        print(str(i)+" "+str(j))
        return [i,j]

