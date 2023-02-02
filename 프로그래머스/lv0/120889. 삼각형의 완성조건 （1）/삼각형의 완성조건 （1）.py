def solution(sides):
    answer = 0
    
    sides.sort(reverse=True)
    
    max_l = sides[0]
    if max_l < sides[1] + sides[2]:
        answer = 1
    else:
        answer = 2
    
    
    return answer