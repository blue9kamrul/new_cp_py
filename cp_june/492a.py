

import sys

# sys.stdout = open('cp_june/output.txt', 'w')
# sys.stdin = open('cp_june/input.txt', 'r')

input = lambda: sys.stdin.readline().strip()
gi = lambda: list(map(int, input().split()))

n = int(input())
height = 0
cubes_needed = 0
level = 1

while cubes_needed <= n:
    cubes_needed_this_level = level * (level + 1) // 2
    if cubes_needed + cubes_needed_this_level <= n:
        cubes_needed += cubes_needed_this_level
        height += 1
        level += 1
    else:
        break

print(height)