import sys
input = sys.stdin.readline

N = int(input())

select = list()

for i in range(N):
    select.append(int(input()))

cnt = 0
m = max(select)

while m != select[0] or select.count(m) >= 2:
    maxIdx = select[1:].index(max(select[1:]))+1
    select[0] += 1
    select[maxIdx] -= 1
    cnt += 1
    m = max(select)

print(cnt)