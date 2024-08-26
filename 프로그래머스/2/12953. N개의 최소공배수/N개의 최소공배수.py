def solution(arr):
    arr = sorted(arr, reverse=True)
    lcm = arr[0]
    
    for num in arr[1:]:
        temp_lcm = lcm
        i = 2
        
        while temp_lcm % num != 0:
            temp_lcm = lcm * i
            i += 1
        
        lcm = temp_lcm
    return lcm