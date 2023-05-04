def solution(str1, str2):
    answer = 0
    while str2 in str1:
        str1 = str1.replace(str2, "")
        answer = 1
        
    
    return answer if answer !=0 else 2