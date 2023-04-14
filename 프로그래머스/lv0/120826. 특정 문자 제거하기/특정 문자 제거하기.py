def solution(my_string, letter):
    answer = []
    
    for i in my_string:
        if i != letter:
            answer.append(i)
    a = ''.join(map(str, answer))
    return a