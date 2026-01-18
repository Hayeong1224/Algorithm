import sys
input = sys.stdin.readline
write = sys.stdout.write
all_elements = [str(i) for i in range(1,21)]

m = int(input())
s = set()

for _ in range(m):
  line = input().split()
  cmd = line[0]
  
  if cmd == "add":
    s.add(line[1])

  elif cmd == "remove":
    s.discard(line[1])

  elif cmd == "check":
    write("1\n" if line[1] in s else "0\n")

  elif cmd == "toggle":
    s.remove(line[1]) if line[1] in s else s.add(line[1])

  elif cmd == "all":
    s.update(all_elements)
      
  else:
    s.clear()