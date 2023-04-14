def solution(angle):
    answer = 0
    angle_dit = {90: 1, 91: 2, 180: 3, 181: 4}
    
    for k, v in angle_dit.items():
        if angle < k :
            answer = v
            break
    return answer