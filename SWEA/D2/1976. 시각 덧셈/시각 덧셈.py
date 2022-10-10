T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    a, b, c, d = map(int, input().split())
    ## 시간은 12 이상이면 다시 1로 변경 예) 13시 면 1시로 변경
    ## 분은 60분 이상이면 시간에 1시간 추가 후 남은 분수만 합계
    
    t = a + c
    m = b + d
    tt = 0
    mm = 0
    if t >= 13:
        t -= 12
    if m >= 60 :
        mm += m -60
        tt += 1
    elif m < 60 :
        mm = m
    sigan = t + tt
    print(f'#{test_case} {sigan} {mm}')