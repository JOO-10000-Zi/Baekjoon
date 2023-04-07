def solution(array):
    answer = 0
    a = sorted(array)
    center = (len(a) // 2) + (len(a) % 2) -1
    answer = a[center]
    return answer