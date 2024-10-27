def dynamic_sliding_window(nums, target):
    win_start = 0
    currSum = 0
    min_win_size = 9999 # maxvalue
    
    for win_end in range(0, len(nums)):
        currSum = currSum + nums[win_end]
    
        while currSum >= target:
            curr_win_size = win_end - win_start + 1
            if curr_win_size == 1:
                return 1
            if curr_win_size < min_win_size:
                min_win_size = win_end - win_start + 1
            currSum = currSum - nums[win_start]
            win_start = win_start + 1
    
    return min_win_size
        
nums = [4, 2, 2, 7, 1 ,1 ,2 , 1, 2]
print(dynamic_sliding_window(nums, 8))

            