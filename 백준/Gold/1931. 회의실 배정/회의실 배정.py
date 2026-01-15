N = int(input())
meetings = [list(map(int, input().split())) for i in range(N)]

# 빨리 끝나는 기준으로 정렬
meetings.sort(key = lambda x: (x[1], x[0]))

count = 0
last_end_time = 0

for start, end in meetings:
  if start >= last_end_time:
    count += 1
    last_end_time = end

print(count)