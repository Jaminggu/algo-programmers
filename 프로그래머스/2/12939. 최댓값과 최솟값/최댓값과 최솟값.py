def solution(s):
    answer = ''
    min_num = 99999
    max_num = -99999
    
    for num in s.split():
        num = int(num)
        
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    
    return str(min_num) + " " + str(max_num)