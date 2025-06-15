import sys

# sys.stdout = open('cp_june/output.txt', 'w')
# sys.stdin = open('cp_june/input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
gs = lambda: input().split()

t = int(input())



for i in range(t):
    n = int(input())
    a = input()
    b = 0
    s = 26 * [False]
    for j in range(n):
        if s[ord(a[j]) - ord('A')] == False:
            s[ord(a[j]) - ord('A')] = True
            b += 1
        b += 1
    print(b)