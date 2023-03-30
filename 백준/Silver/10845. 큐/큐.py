from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

dq = deque()
for _ in range(T):
    word = input().split()

    if len(word) > 1:
        dq.append(word[1])
    elif word[0] == "pop":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif word[0] == "size":
        print(len(dq))
    elif word[0] == "empty":
        if dq:
            print(0)
        else:
            print(1)
    elif word[0] == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif word[0] == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)
