import math
def solution(n, s):
    if n > s:
        return [-1]
    
    base = s // n
    remainder = s % n
    
    answer = [base] * n
    
    for i in range(remainder):
        answer[n-1-i] += 1
        
    return answer