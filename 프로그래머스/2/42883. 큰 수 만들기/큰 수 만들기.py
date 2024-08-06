def solution(number, k):
    num_list = []
    
    for num in number:
        while num_list and num_list[-1] < num and k > 0:
            num_list.pop()
            k -= 1
        num_list.append(num)
    num_list = num_list[:len(num_list) - k]
    
    return ''.join(num_list)