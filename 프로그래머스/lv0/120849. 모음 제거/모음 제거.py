def solution(my_string):
    answer = ''
    list1 = ['a', 'e','i','o','u']
    
    for i in my_string:
        if i in list1:
            answer += ""
        else:
            answer += i
    return answer