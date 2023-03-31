import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    word = input().split()

    answer = ' '.join(map(str, word[::-1]))
    print(f'Case #{i+1}: {answer}')


