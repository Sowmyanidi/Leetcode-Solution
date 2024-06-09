def maximumGap(nums):
    if len(nums)<2:
        return 0
    elif len(nums) == 2:
        return max(nums)-min(nums)
    else:
        new = [0]*len(nums)
        count = [0]*(max(nums)+1)
        for i in nums:
            count[i]+=1

        for i in range(1, len(count)):
            count[i]+=count[i-1]
            
        for i in range(len(nums)-1, -1, -1):
            count[nums[i]] -=1
            new[count[nums[i]]] = nums[i]
        
        print(new)

        max_count = 0

        for i in range(1,len(nums)):
            x = new[i]-new[i-1]
            max_count = max(x, max_count)
        return max_count
    
print(maximumGap([3,6,1,7,9,2]))