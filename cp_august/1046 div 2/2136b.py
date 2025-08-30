import sys

sys.stdout = open('cp_august/output.txt', 'w')
sys.stdin = open('cp_august/input.txt', 'r')

input = sys.stdin.readline
 
gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input())