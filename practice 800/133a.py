import sys

# sys.stdout = open('cp_august/output.txt', 'w')
# sys.stdin = open('cp_august/input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
gs = lambda: input().split()

p = input()
c = 0

for i in range(len(p)):
    if p[i] == 'H' or p[i] == 'Q' or p[i] == '9':
        print("YES")
        c = 0
        break
    else:   
        c += 1

if c != 0:  
    print("NO")
