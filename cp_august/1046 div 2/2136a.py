import sys

# sys.stdout = open('cp_august/output.txt', 'w')
# sys.stdin = open('cp_august/input.txt', 'r')

input = sys.stdin.readline
 
gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for _ in range(t):
    a = gi()
    if max(a[0],a[1]) <= (2 * (min(a[0],a[1]) + 1)):
        if max((a[2] - a[0]),(a[3] - a[1])) <= (2 * (min(a[2] - a[0],a[3] - a[1]) + 1)):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
    