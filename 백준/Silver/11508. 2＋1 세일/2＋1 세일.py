N = int(input())

uoosan = []
sum_pay = 0

for _ in range(N):
    pay = int(input())
    uoosan.append(pay)

uoosan_sort = sorted(uoosan, reverse=True)
for i in range(len(uoosan_sort)):
    if i % 3 < 2:
        sum_pay += uoosan_sort[i]

print(sum_pay)