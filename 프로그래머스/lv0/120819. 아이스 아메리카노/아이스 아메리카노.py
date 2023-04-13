def solution(money):
    answer = []
    get = money//5500
    remoney = money%5500
    answer.append(get)
    answer.append(remoney)
    return answer