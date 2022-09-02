N, M = map(int, input().split())

p = True
for _ in range(M):
    book1 = int(input())
    book1_list = list(map(int, input().split()))
    for i in range(book1 - 1):
        if book1_list[i] < book1_list[i+1]:
            p = False
            break
    if not p : break

print('Yes' if p else 'No')
    