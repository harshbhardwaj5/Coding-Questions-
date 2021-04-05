1)--------------------------
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
       int maxx=0;
       int curr=nums[0];
         for (int n : nums)
         {
             if(maxx<0)
                maxx=0;
            maxx+=n;
            curr=max(curr,maxx);
        
                
                 
                 
         }
        return curr;
        
    }
};


2)---------------------------
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<=0:
            return -1 
        elif len(nums)==1: 
            return nums[0]
        num
        else:    
            for i in range(1, len(nums)):
                if nums[i-1] > 0:
                    nums[i] += nums[i-1]
        return max(nums)


        