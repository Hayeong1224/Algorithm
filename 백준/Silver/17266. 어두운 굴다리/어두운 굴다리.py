n = int(input())
m = int(input())
locs = list(map(int, input().split()))

h = max(locs[0] - 0, n - locs[-1])
is_passed, prev = False, 0
while not is_passed:
  for i, loc in enumerate(locs):
    if prev < loc and loc - prev > h:
      h += 1
      break

    else:
      prev = loc + h

    if prev >= n:
      is_passed = True
  
print(h)