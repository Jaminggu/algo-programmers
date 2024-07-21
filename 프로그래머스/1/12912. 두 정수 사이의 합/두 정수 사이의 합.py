def solution(a, b):
    answer = 0
    
    for x in range(min(a, b), max(a, b) + 1): answer += x
    
    return answer