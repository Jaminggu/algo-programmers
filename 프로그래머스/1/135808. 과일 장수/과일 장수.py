def solution(k, m, score):
    answer = 0
    score.sort()
    apples = []
    
    while len(score) >= m:
        for _ in range(m): apples.append(score.pop())
        answer += apples[-1] * m
        
    return answer