import sys

# sys.stdout = open('cp_august/output.txt', 'w')
# sys.stdin = open('cp_august/input.txt', 'r')

input = sys.stdin.readline
 
gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for _ in range(t):
    s = set()
    c = 1
    n = int(input())
    a = gi()
    for i in range(n):
        s.add(a[i])
    if n - len(s) >= 1:
        print("yes")
    else:
        print("no")
