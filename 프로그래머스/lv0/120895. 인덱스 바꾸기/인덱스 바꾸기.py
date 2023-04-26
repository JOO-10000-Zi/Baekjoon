def solution(my_string, num1, num2):
    answer = ''
    a = ""
    b = ""
    for i in range(len(my_string)):
        if i == num1 :
            a = my_string[i]
            answer += my_string[num2]
        elif i == num2 :
            b = my_string[i]
            answer += my_string[num1]
        else:
            answer += my_string[i]
                 
    return answer