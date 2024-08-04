def solution(X, Y):
    answer = ''
    count_X = {}
    count_Y = {}
    
    for x in X:
        if x in count_X:
            count_X[x] += 1
        else:
            count_X[x] = 1
            
    for y in Y:
        if y in count_Y:
            count_Y[y] += 1
        else:
            count_Y[y] = 1
    
    num_list = []
    
    for count_x in count_X:
        if count_x in count_Y:
            for _ in range(min(count_X[count_x], count_Y[count_x])):
                num_list.append(count_x)

    if len(num_list) == 0: 
        return "-1"
    elif all(num == "0" for num in num_list):
        return "0"
        
    answer = ''.join(sorted(num_list, reverse = True))
        
    return answer