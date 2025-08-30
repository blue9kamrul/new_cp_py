import sys

# sys.stdout = open('cp_august/output.txt', 'w')
# sys.stdin = open('cp_august/input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
gs = lambda: input().split()

n = int(input())
r = 0

for i in range(n):
    a, b, c = gi()
    if a + b + c > 1:
        r += 1

print(r)