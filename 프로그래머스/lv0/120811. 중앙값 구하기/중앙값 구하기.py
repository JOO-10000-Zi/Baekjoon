def solution(array):
    answer = 0
    a = sorted(array)
    center = (len(a) // 2)
    answer = a[center]
    return answer