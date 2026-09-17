def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        time = 0
        
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                time += 1
            else:
                time += 1 # 다음까지 떨어지진 않았으니 +1 & 더 이상 측정 x
                break
        
        answer[i] = time
        
    return answer

# 가격이 떨어지지 않은 기간은 몇 초인지