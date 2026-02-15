def dfs(seq, m):
  if m == 0:
    ans.append(list(seq))
    return

  for a in array:
    if a not in seq:
      if not seq or (seq and a > max(seq)):
        seq.append(a)
        dfs(seq, m-1)
        seq.remove(a)
  return

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
ans = list()

dfs([], m)
for seq in ans:
  print(*seq)