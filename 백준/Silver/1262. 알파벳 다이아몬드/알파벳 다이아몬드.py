n, r1, c1, r2, c2 = map(int, input().split())

for i in range(r1, r2+1):
  row_str = ""
  for j in range(c1, c2+1):
    ni = i % (2*n -1)
    nj = j % (2*n -1)
    
    dist = abs((n-1)-ni) + abs((n-1)-nj)

    if dist >= n:
      row_str += '.'
    else:
      row_str += chr(ord('a') + (dist%26))
  print(row_str)