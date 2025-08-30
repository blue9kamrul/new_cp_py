import sys
import math

sys.stdout = open('cp_august/output.txt', 'w')
sys.stdin = open('cp_august/input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
gs = lambda: input().split()

n, k = gi()
b = gi()
c = 0

for i in range(len(b)):
    if b[i] > k and b[i] > 0:
        c += 1

print(c)
