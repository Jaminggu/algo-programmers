def solution(k, score):
    answer = []
    array = []
    
    for i in range(len(score)):
        array.append(score[i])
        array.sort()
        if(len(array) > k):
            array.pop(0)
        answer.append(array[0])
        
    
    return answer