def solution(array):
    a = {}
    cnt = 0
    for i in array:
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
            
    z = max(a.values())
    result = 0
    for k, v in a.items():
        if a[k] == z :
            result = k
            cnt += 1

    if cnt > 1:
        return -1
    else:
        return result

        