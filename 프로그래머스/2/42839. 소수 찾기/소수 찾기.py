from itertools import permutations
import math

# 소수 판별
def is_prime(num):
    if num < 2: 
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    new_numbers = [n for n in numbers] # 한 글자씩
    
    # 모든 경우의 수 만들기
    candidates = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(new_numbers, i):
            candidates.add(int(''.join(p)))
    
    return sum(1 for c in candidates if is_prime(c)) 