import sys

# sys.stdout = open('cp_june/output.txt', 'w')
# sys.stdin = open('cp_june/input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
t = int(input())
for _ in range(t):
    n = int(input())
    a = gi()
    
    total_sum = sum(a)
    
    if total_sum % 2 == 0:
        print("YES")
    else:
        print("NO")
