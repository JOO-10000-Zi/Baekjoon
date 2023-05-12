def solution(my_str, n):
    answer = []
    cnt = 0
    a = ""
    for i in my_str:
        a += i
        if len(a) == n:
            answer.append(a)
            a = ""
    if a != "":
        answer.append(a)
            

    
    return answer