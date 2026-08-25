nums=[7,11,2]
target=9

for i in range(len(nums)):# i got the index of the first number
    for j in range(i+1,len(nums)):# j  got the index of the second number, if take index(0), range(i+1, len(nums))
        if nums[i]+nums[j]==target:# if the sum of the two numbers equals the target
            print([i,j])