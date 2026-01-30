from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  W = input().strip() # 양옆 공백과 개행 문자 제거
  K = int(input())

  if K == 1:
    print(1,1)
    continue

  # 알파벳별 등장 인덱스 저장
  char_dict = defaultdict(list)
  for i in range(len(W)):
    char_dict[W[i]].append(i)

  min_len = float('inf')
  max_len = -1

  # 알파벳별 조건에 맞는 길이 구하기
  for char in char_dict:
    indices = char_dict[char]
    if len(indices) >= K:
      for i in range(len(indices) - K + 1):
        length = indices[i+K-1] - indices[i] + 1
        min_len = min(min_len, length)
        max_len = max(max_len, length)

  if max_len == -1:
    print(-1)
  else:
    print(min_len, max_len)