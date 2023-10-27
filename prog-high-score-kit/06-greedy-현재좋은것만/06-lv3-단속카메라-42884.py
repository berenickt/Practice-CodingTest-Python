# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42884
"""
고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 
단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.

고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 
모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 
최소 몇 대의 카메라를 설치해야 하는지를 return

입력 #1
[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

출력 #1
2

-5 지점에 카메라를 설치하면 두 번째, 네 번째 차량이 카메라를 만납니다.
-15 지점에 카메라를 설치하면 첫 번째, 세 번째 차량이 카메라를 만납니다.
"""


def solution(routes):
    cameraCnt = 0

    # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    routes.sort(key=lambda x: x[1])

    # 최대 -30000이니 초기 카메라 위치를 -30001로 초기화
    camera = -30001

    ### 카메라가 진입 지점(route[0])보다 작은지 확인
    # 작다면, 현재 카메라 위치로 해당 차량을 만나지 못했다는 의미
    # - 카메라를 추가로 세우고
    # - 가장 최근 카메라의 위치(route[1])를 갱신
    for route in routes:
        if camera < route[0]:
            cameraCnt += 1
            camera = route[1]
    return cameraCnt


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
