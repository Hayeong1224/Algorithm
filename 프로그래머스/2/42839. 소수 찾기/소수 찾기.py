from itertools import permutations
import math

def isPrimeNumber(num): # 소수 판별
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: 
            return False
        
    return True

def solution(numbers):
    lst = [c for c in numbers]
    
    # 모든 경우의 수 만들어 소수 판별
    ans = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(lst, i):
            num = int(''.join(p))
            if num not in ans and isPrimeNumber(num):
                ans.add(num)
    
    return len(ans)