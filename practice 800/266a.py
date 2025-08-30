import sys

# sys.stdout = open('cp_august/output.txt', 'w')
# sys.stdin = open('cp_august/input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
gs = lambda: input().split()

n = int(input())

s = input()
c = 0
for i in range(n-1):
    if s[i] == s[i+1]:
        c += 1
print(c)