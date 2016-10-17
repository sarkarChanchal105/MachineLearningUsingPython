"""
https://leetcode.com/problems/two-sum/

"""

class Solution(object):
    def twoSum(self, nums, target):
        sorted_nums= sorted(nums)
        begin = 0
        end= len(sorted_nums)-1
        values=[]
        while (begin<=end):
                print (begin,end)
                if (sorted_nums[begin]+sorted_nums[end]==target):
                    values= [sorted_nums[begin],sorted_nums[end]]
                    if sorted_nums[begin]==sorted_nums[end]:
                        first=nums.index(values[0])
                        nums.pop(values[0])
                        second=nums.index(values[1])+1
                        return(first,second)
                    else:

                        first=nums.index(values[0])
                        second=nums.index(values[1])
                        return(first,second)

                if (sorted_nums[begin]+sorted_nums[end])> target:
                    end=end-1
                if (sorted_nums[begin]+sorted_nums[end])< target:
                    begin=begin+1



k= Solution()

nums =[0,4,3,0]
target = 0

print(k.twoSum(nums,target))
