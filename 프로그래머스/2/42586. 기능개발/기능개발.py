def solution(progresses, speeds):
    answer = []
    
    while progresses:
        cnt = 0
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        while progresses and progresses[0] >= 100:
            del progresses[0], speeds[0]
            cnt += 1
            
        if cnt > 0: answer.append(cnt)
    
    return answer