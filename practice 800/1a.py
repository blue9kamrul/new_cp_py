import sys
import math

# sys.stdout = open('cp_august/output.txt', 'w')
# sys.stdin = open('cp_august/input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))
gs = lambda: input().split()


a = gi()
    
length = math.ceil(a[0] / a[2])
width = math.ceil(a[1] / a[2])

print(length * width)