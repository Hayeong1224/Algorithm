def solve():
  N, M = map(int, input().split())
  A = [int(input()) for _ in range(N)]
  A.sort()
  
  left, right = 0, 0
  ans = float('inf')

  while right < N and left < N:
    gap = A[right] - A[left]

    if gap < M:
      right += 1

    elif gap == M:
      print(M)
      return

    else:
      ans = min(ans, gap)
      left += 1

      if left > right:
        right = left

  print(ans)
  
solve()