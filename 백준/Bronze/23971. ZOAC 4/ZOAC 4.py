import math

h, w, n, m = map(int, input().split())

row_count = math.ceil(h/(n+1))
col_count = math.ceil(w/(m+1))

print(row_count * col_count)