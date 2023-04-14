def solution(age):
    answer = ''
    age_list = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9}
    
    for i in str(age):
        for k, v in age_list.items():
            if int(i) == v:
                answer += k
    
    return answer
