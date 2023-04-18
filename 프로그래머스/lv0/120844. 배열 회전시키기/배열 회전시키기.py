def solution(numbers, direction):
    answer = []
    L = len(numbers)
    if direction == "right":
        R = numbers.pop()
        numbers.insert(0, R)
        answer = numbers
    else:
        le = numbers[0]
        numbers.remove(le)
        numbers.insert(L, le)
        answer = numbers
        
    return answer