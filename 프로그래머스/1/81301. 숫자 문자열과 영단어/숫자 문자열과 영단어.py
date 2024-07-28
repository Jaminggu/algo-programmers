def solution(s):
    answer = ''
    temp = ''
    
    for c in s:
        if c in '0123456789':
            answer += c
        else: temp += c
        
        if temp == 'zero':
            answer += '0'
            temp = ''
        elif temp == 'one':
            answer += '1'
            temp = ''
        elif temp == 'two':
            answer += '2'
            temp = ''
        elif temp == 'three':
            answer += '3'
            temp = ''
        elif temp == 'four':
            answer += '4'
            temp = ''
        elif temp == 'five':
            answer += '5'
            temp = ''
        elif temp == 'six':
            answer += '6'
            temp = ''
        elif temp == 'seven':
            answer += '7'
            temp = ''
        elif temp == 'eight':
            answer += '8'
            temp = ''
        elif temp == 'nine':
            answer += '9'
            temp = ''
    
    return int(answer)