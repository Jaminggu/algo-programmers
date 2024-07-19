def solution(n):
    i = 1
    
    while True:
        if(i * i == n): return (i+1) * (i+1)
        if(n // 2 < i): break 
        i += 1
        
    return -1