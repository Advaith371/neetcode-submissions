class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=defaultdict(list)
        nums.sort()
        for i in  range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l < r :
                total=nums[i]+nums[l]+nums[r]

                if total < 0:
                    l+=1 
                elif total >0 :
                    r-=1 
                else :
                    if tuple([nums[i],nums[l],nums[r]]) not in res:
                        res[tuple([nums[i],nums[l],nums[r]])].append(nums[i])
                        res[tuple([nums[i],nums[l],nums[r]])].append(nums[l])
                        res[tuple([nums[i],nums[l],nums[r]])].append(nums[r])
                    l+=1
                    r-=1
        return list(res.values())