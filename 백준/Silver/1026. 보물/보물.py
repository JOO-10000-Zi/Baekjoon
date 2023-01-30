N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

min_sum = 0
for i in range(N):
    min_sum += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(min_sum)
