import sys

sys.stdout = open('cp_august/output.txt', 'w')
sys.stdin = open('cp_august/input.txt', 'r')

input = sys.stdin.readline
 
gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())

for _ in range(t):
    c = 0
    n = int(input())
    a = gi()
    i = 0
    for i in range(0,n - 2, 2):
        c += max(a[i], a[i+1])
        if (a[i] - min(a[i], a[i+1])) < 0:
            a[i] = 0
        else:
            a[i] -= min(a[i], a[i+1])
        if (a[i+1] - min(a[i], a[i+1])) < 0:
            a[i+1] = 0
        else:
            a[i+1] -= min(a[i], a[i+1])
    mn = min(a)
        
        


    
