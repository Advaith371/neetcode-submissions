class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valid=0
        i=0
        while valid!=1:
        
            needed=target-nums[i]
            new=nums.copy()
            new[i]=None

            if needed in new:
                valid=1
                return [i,new.index(needed)]
              
            else: i=i+1
        