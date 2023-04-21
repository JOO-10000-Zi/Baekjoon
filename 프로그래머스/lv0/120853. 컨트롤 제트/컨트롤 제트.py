def solution(s):
    answer = 0
    a = s.split()
    for i in range(len(a)):
        if a[int(i)] != "Z":
            answer += int(a[int(i)])
        else:
            answer -= int(a[int(i)-1])
        
        
    return answer