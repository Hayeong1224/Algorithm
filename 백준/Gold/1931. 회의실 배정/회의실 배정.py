n = int(input())
meetings = sorted([list(map(int, input().split())) for _ in range(n)], key= lambda x : (x[1], x[0])) # [start, end] end 기준으로 정렬

cnt, prev = 0, 0 
for start, end in meetings:
  if start >= prev:
    cnt += 1
    prev = end

print(cnt)