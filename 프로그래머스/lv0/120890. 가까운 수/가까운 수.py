def solution(array, n):
    answer = 0
    c = n + 100
    array.sort()
    for i in array:
        if c > abs(n - i):
            c = abs(n - i)
            answer = i
    return answer