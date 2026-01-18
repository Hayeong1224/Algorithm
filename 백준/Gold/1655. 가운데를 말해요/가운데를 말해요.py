import heapq
import sys

input = sys.stdin.readline
n = int(input())

left_heap = []
right_heap = []

for _ in range(n):
  num = int(input())

  # 균형 맞춰 넣기
  if len(left_heap) == len(right_heap):
    heapq.heappush(left_heap, -num)
  else:
    heapq.heappush(right_heap, num)

  # 왼쪽 최댓값이 오른쪽 최솟값보다 크면 교체
  if right_heap and (-left_heap[0] > right_heap[0]):
    left_val = -heapq.heappop(left_heap)
    right_val = heapq.heappop(right_heap)

    heapq.heappush(left_heap, -right_val)
    heapq.heappush(right_heap, left_val)

  print(-left_heap[0])