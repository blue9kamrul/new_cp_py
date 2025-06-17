
import sys


# sys.stdout = open('cp_june/output.txt', 'w')
# sys.stdin = open('cp_june/input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
gs = lambda: input().split()

t = int(input())

for _ in range(t):
    n = int(input())
    a = gi()

    c = 0           
    res = 0         

    i = 0
   
   
    # while i < n and a[i] == 0:
    #     i += 1

    # Traverse from the first 1 onwards
    # i += 1
    # print("ff",i)
    while i < n:
        if a[i] == 0:
            c += 1
        else:
            res = max(res, c)
            c = 0
        i += 1

    print(max(c,res))
