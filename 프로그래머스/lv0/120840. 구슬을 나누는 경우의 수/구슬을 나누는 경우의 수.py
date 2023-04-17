from math import factorial as fac

def solution(balls, share):
    n = fac(balls)
    m = fac(share)
    nm = fac(balls-share)
    
    answer = n/(nm*m)
    
    return answer