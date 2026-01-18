import sys
input = sys.stdin.readline
n = int(input())
a = n // 3
b = n % 3
print("SK" if (a+b)%2==1 else "CY")