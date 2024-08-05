def solution(n, lost, reserve):
    lost_num = len(lost)
    
    intersection = list(set(lost) & set(reserve))
    lost_num -= len(intersection)
    
    if intersection:
        for inter in intersection:
            lost.remove(inter)
            reserve.remove(inter)
    
    lost.sort()
    reserve.sort()
    
    for i in lost:
        for j in reserve:
            if j - 1 <= i <= j + 1:
                lost_num -= 1
                reserve.remove(j)
                break
    
    return n - lost_num