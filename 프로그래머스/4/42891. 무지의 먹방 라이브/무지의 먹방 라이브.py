import heapq

def solution(food_times, k):
    
    if sum(food_times) < k + 1: return -1

    # (음식 시간, 번호) 형태로 우선순위 큐에 삽입
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    remain = len(food_times) # 남은 음식의 개수

    # (sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수)와 k 비교
    while sum_value + ((q[0][0] - previous) * remain) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * remain
        remain -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1]) 
    return result[(k - sum_value) % remain][1]