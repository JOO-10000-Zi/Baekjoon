def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit() != True:
            my_string = my_string.replace(i, ",")
            
    a = list(map(str, my_string.split(",")))
    for i in a:
        if i.isdigit() :
            answer += int(i)
            
    return answer