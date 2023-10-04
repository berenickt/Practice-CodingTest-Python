# 📚 https://school.programmers.co.kr/learn/courses/30/lessons/181946
# 방법1
print(input().strip().replace(" ", ""))

# 방법2
str1, str2 = input().strip().split(" ")
print(f"{str1}{str2}")
