import sys
import math

sys.stdout = open('cp_august/output.txt', 'w')
sys.stdin = open('cp_august/input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
gs = lambda: input().split()

n = int(input())
if n == 2:
    print("NO")
elif n % 2 == 0:
    print("YES")
else:
    print("NO")