# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 
각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 
뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 
이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 
각 배포마다 몇 개의 기능이 배포되는지를 return

입력 #1
progresses  : [93, 30, 55]
speeds      : [1, 30, 5]

출력 #1
[2, 1]

입출력 예 설명 #1
첫 번째 기능은 93% 완료되어 있고 
하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능

두 번째 기능은 30%가 완료되어 있고 
하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능
하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포

세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 
9일간 작업 후 배포가 가능
"""


def solution(progresses, speeds):
    answer = []
    days = 0
    feat_count = 0

    while len(progresses) > 0:
        # 기능의 진행상황과 그 동안 지난 날짜만큼의 speed를 구해서 더하기
        if (progresses[0] + days * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            feat_count += 1

        else:
            # 만약 완료된 기능이 있다면 answer에 더해주고 0으로 초기화
            if feat_count > 0:
                answer.append(feat_count)
                feat_count = 0
            # 완료된 기능이 없으면 days 추가
            days += 1
    answer.append(feat_count)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))


def solution(progresses, speeds):
    Q = []
    for pro, spe in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((pro - 100) // spe):
            Q.append([-((pro - 100) // spe), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]
