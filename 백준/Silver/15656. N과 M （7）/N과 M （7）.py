def dfs(seq, arr, M):
  if len(seq) == M:
    print(*seq)
    return

  for num in arr:
    seq.append(num)
    dfs(seq, arr, M)
    seq.pop()

  return

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

dfs([], arr, M)