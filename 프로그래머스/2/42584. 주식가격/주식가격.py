def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i in range(n):
        # 가격이 떨어졌다면, 그 전의 모든 가격들을 POP하며 시간 계산
        while stack and stack[-1][0] > prices[i]:
            price, idx = stack.pop()
            answer[idx] = i - idx
            
        stack.append((prices[i], i))
        
    # 끝까지 가격이 떨어지지 않은 나머지
    while stack:
        price, idx = stack.pop()
        answer[idx] = (n-1) - idx
    
    return answer