def solution(rsp):
    answer = ''
    a = "2"
    b = "0"
    c = "5"
    
    for i in str(rsp) :
        if i == a:
            answer += b
        elif i == b :
            answer += c
        else:
            answer += a
    return answer