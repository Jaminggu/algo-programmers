from collections import deque

def solution(n, m, section):
    answer = 0
    dq = deque(section)
    
    while dq:
        start = dq.popleft()
        answer += 1
        while dq and dq[0] < start + m: 
            dq.popleft()
    
    return answer