from collections import deque 

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    index = deque(range(len(priorities)))
    
    while priorities:
        maxP = max(priorities)
        
        if priorities[0] == maxP:
            priorities.popleft()
            answer += 1
            if index.popleft() == location:
                break
        else:
            priorities.append(priorities.popleft())
            index.append(index.popleft())
        
    return answer