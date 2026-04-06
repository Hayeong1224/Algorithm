def solution(word): 
    # 5번째 자리: 가중치 1
    # 4번째 자리: 가중치 6 (1 * 5 + 1)
    # 3번째 자리: 가중치 31 (6 * 5 + 1)
    # 2번째 자리: 가중치 156 (31 * 5 + 1)
    # 1번째 자리: 가중치 781(156 * 5 + 1)   
    
    weights = [781, 156, 31, 6, 1]
    vowels = "AEIOU"
    
    ans = 0
    for i in range(len(word)):
        idx = vowels.index(word[i])
        
        ans += idx * weights[i] + 1
        
    return ans