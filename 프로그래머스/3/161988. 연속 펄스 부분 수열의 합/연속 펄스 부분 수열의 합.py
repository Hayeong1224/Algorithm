def solution(sequence):
    # 연속 펄스 수열로 만들기
    n = len(sequence)
    prefix_sum = [0] * (n+1)
    mul = -1
    for i in range(n):
        prefix_sum[i+1] = (prefix_sum[i] + sequence[i] * mul)
        mul *= -1
        
    # 최대 합 구하기
    return max(prefix_sum) - min(prefix_sum)