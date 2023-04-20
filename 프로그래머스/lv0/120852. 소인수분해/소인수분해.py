def solution(n):
    answer = []
    a = 2
    
    while a <= n:
        if n % a == 0:
            answer.append(a)
            n = n // a
        else:
            a += 1
    
    return list(dict.fromkeys(answer))