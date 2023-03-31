import sys

input = sys.stdin.readline

T = int(input())

stk = []
cnt = 1
for _ in range(T):
    stk.append(int(input()))

Max = stk[-1]

for i in range(len(stk)-1, -1, -1):
    if stk[i] > Max:
        cnt += 1
        Max = stk[i]

print(cnt)

