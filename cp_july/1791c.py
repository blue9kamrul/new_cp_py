import sys

# sys.stdout = open('cp_july/output.txt', 'w')
# sys.stdin = open('cp_july/input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input()))
gs = lambda: input().split()

t = int(input())

for i in range(t):
    n = int(input())
    s = list(input())
    

    for j in range(n//2):
        if (s[-1] == '1' and s[0] == '0') or (s[-1] == '0' and s[0] == '1'):
            n -= 2
            s.pop(-1)
            s.pop(0)

    print(n)