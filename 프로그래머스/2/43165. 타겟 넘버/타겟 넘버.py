def solution(numbers, target):
    def dfs(num, idx):
        if idx == len(numbers):
            if num == target:
                return 1
            return 0
        
        add = dfs(num + numbers[idx], idx + 1)
        subtract = dfs(num - numbers[idx], idx + 1)
        
        return add + subtract

    return dfs(0, 0)
