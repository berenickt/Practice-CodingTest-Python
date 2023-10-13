# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181836
"""
직사각형 형태의 그림 파일이 있고,
이 그림 파일은 1 x 1 크기의 정사각형 크기의 픽셀로 이루어져 있습니다.
이 그림 파일을 나타낸 문자열 배열 picture과 정수 k가 매개변수로 주어질 때,
이 그림 파일을 가로 세로로 k배 늘린 그림 파일을 나타내도록 문자열 배열을 return

입력#1
picture : [
            ".xx...xx.",
            "x..x.x..x",
            "x...x...x",
            ".x.....x.",
            "..x...x..",
            "...x.x...",
            "....x....",
          ],
k       : 2

출력#1
[
  "..xxxx......xxxx..",
  "..xxxx......xxxx..",
  "xx....xx..xx....xx",
  "xx....xx..xx....xx",
  "xx......xx......xx",
  "xx......xx......xx",
  "..xx..........xx..",
  "..xx..........xx..",
  "....xx......xx....",
  "....xx......xx....",
  "......xx..xx......",
  "......xx..xx......",
  "........xx........",
  "........xx........",
]
"""


def solution(picture, k):
    zoom_in = []
    for pixel in picture:
        new_pixel = ""
        for p in pixel:
            new_pixel += p * k  # k배씩 추가
        zoom_in.append(new_pixel)
    return [s for s in zoom_in for _ in range(k)]


print(
    solution(
        [
            ".xx...xx.",
            "x..x.x..x",
            "x...x...x",
            ".x.....x.",
            "..x...x..",
            "...x.x...",
            "....x....",
        ],
        2,
    )
)


#############################
def solution2(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace(".", "." * k).replace("x", "x" * k))
    return answer
