def solution(s):
    answer = 0
    
    for i in range(len(s)):
        stack = []
        checked = True
        s_rotated = s[i:] + s[:i]
        
        for j in s_rotated:
            if j in '[({':  
                stack.append(j)
            elif j in '])}': 
                if not stack:  
                    checked = False
                    break
                elif j == ')' and stack[-1] == '(': 
                    stack.pop()
                elif j == ']' and stack[-1] == '[':
                    stack.pop()
                elif j == '}' and stack[-1] == '{':
                    stack.pop()
                else: 
                    checked = False
                    break
        if checked and not stack:
            answer += 1
            
    return answer