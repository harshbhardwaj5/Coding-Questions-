#Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
# 1)Count fucntion
#         c=[0]*100000
#         k=[]
#         for i in range(len(nums)):
#             c[nums[i]]+=1 
#         for i in range(len(c)):
#             if c[i]==2:
#                 k.append(i)
                
#         return k

# 2) Approach using Dictionary
#         k={}
#         ls=[]
#         for i in range(len(nums)):
#             k[nums[i]] = k.get(nums[i],0)+1
           
 
#         # print(k)
#         for i in k:
#             if k[i]==2:
#                 ls.append(i)
#         return ls

# # 3)Negative Indexes
#         ls=[]
#         for i in range(len(nums)):
#             i=abs(nums[i])-1
#             if nums[i]<0:
#                 ls.append(i+1)
          
#             nums[i]= -nums[i]
            
            
#         return ls