import sys

# sys.stdout = open('cp_august/output.txt', 'w')
# sys.stdin = open('cp_august/input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
gs = lambda: input().strip()

n = int(input())
x = 0
s = []

for i in range(n):
    s.append(input().strip())
    if "--" in s[i]:
        x -= 1
    elif "++" in s[i]:
        x += 1
print(x)
