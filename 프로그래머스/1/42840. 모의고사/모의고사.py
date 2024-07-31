from collections import deque

def solution(answers):
    answer = []
    scores = [0, 0, 0]
    arr1 = deque([1, 2, 3, 4, 5])
    arr2 = deque([2, 1, 2, 3, 2, 4, 2, 5])
    arr3 = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    
    for ans in answers:
        if ans == arr1[0]: 
            scores[0] += 1
        if ans == arr2[0]: 
            scores[1] += 1
        if ans == arr3[0]:
            scores[2] += 1
        arr1.append(arr1.popleft())
        arr2.append(arr2.popleft())
        arr3.append(arr3.popleft())

    for i in range(len(scores)):
        if scores[i] == max(scores):
            answer.append(i + 1)

    return answer;