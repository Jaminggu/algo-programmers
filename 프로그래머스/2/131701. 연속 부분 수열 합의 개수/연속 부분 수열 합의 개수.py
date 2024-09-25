def solution(elements):
    answer = 0
    e_dupli = elements * 2
    elements_set = set()
    
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            elements_set.add(sum(e_dupli[j:j+i]))
    
    return len(elements_set)

