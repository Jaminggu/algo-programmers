def solution(s):
    answer = 0
    
    start = s[0]
    same = 0
    different = 0
    
    for i in range(len(s)):
        if s[i] == start:
            same += 1
        else: different += 1
        
        if same == different:
            same = 0
            different = 0
            answer += 1
            if i + 1 < len(s):
                start = s[i + 1]   
                
    if same != 0 or different != 0:
        answer += 1        
    
    return answer