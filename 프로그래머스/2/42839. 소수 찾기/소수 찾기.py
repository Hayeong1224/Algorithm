from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    num = [i for i in numbers]
    candidates = set()
    
    # 만들 수 있는 경우의 수 순열 -> 소수 판별 돌리기
    for i in range(1, len(numbers) + 1):
        for p in permutations(num, i):
            candidates.add(int(''.join(p)))
            
    return sum(1 if is_prime(n) else 0 for n in candidates)