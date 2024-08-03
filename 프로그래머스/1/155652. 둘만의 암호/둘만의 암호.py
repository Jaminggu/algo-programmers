def solution(s, skip, index):
    answer = ''
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabets = [a for a in alphabets if a not in skip]
    
    for char in s:
        answer += alphabets[(alphabets.index(char) + index) % len(alphabets)]
    
    return answer