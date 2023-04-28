def solution(num, k):
    answer = 0
    a = str(num)
    for i in range(len(a)):
        if str(k) not in a:
            answer = -1
        else:
            if a[i] == str(k):
                answer = i +1
                break
                                        
    return answer