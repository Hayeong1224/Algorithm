N, S = map(int, input().split())
seq = list(map(int, input().split()))

count = 0
def dfs(idx, sum):
  global count
  
  if idx == N:
    return

  # 현재 원소를 포함하는 경우
  if sum + seq[idx] == S:
    count += 1

  dfs(idx + 1, sum + seq[idx])
  dfs(idx + 1, sum)    

dfs(0,0)
print(count)