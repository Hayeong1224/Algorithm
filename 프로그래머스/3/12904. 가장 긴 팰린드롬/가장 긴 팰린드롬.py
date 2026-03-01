def solution(s):
    answer = 0
    n = len(s)
    if n < 2: return n

    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(n):
        len1 = expand(i,i) # 홀수 길이
        len2 = expand(i, i + 1) # 짝수 길이
        
        answer = max(answer, len1, len2)
    
    return answer