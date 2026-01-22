N = int(input())
A = list(map(int,input().split()))
B, C = map(int, input().split())

ans = 0
for i in range(N):
  ans += 1 # 총감독관 1명
  remained = A[i] - B
  if remained > 0:
    ans += (remained + C - 1) // C

print(ans)