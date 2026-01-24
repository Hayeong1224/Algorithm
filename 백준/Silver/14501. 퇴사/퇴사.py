def dfs(date, total_price):
  global ans
  if date == len(counsels):
    ans = max(ans, total_price)
    return
    
  t, p = counsels[date]
  # 선택 x
  dfs(date+1, total_price)
  # 선택 o
  if date+t <= len(counsels):
    dfs(date+t, total_price + p)

n = int(input())
counsels = [list(map(int, input().split())) for _ in range(n)] # [시간, 금액]

ans = 0
dfs(0,0)
print(ans)