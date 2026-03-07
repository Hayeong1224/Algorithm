def solution(n, k):
    ans = 12000 * n + 2000 * k
    ans -= 2000 * (n // 10)
    return ans