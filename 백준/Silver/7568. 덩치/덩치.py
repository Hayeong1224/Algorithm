n = int(input())
bodies = [list(map(int, input().split())) for _ in range(n)]

ans = []
for i in range(n):
  count = 0
  for j in range(n):
    if i == j:
      continue
    if bodies[i][0] < bodies[j][0] and bodies[i][1] < bodies[j][1]:
      count += 1
  ans.append(count+1)

print(*ans)