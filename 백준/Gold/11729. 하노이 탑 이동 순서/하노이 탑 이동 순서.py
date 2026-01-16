def hanoi(n, start, end, sub):
  if n == 1:
    print(start, end)
    return

  # n-1개를 start -> sub
  hanoi(n-1, start, sub, end)

  # 큰 원판을 start -> end
  print(start, end)

  # n-1개를 sub -> end
  hanoi(n-1, sub, end, start)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3, 2)