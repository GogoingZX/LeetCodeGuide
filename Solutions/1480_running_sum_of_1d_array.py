def solution(nums):
    # nums: list-like

    count = 0
    size = len(nums)
        
    temp_result = 0
    final_results = []
    while count < size:
        temp_result += nums[count]
        final_results.append(temp_result)
        count += 1
    
    return final_results