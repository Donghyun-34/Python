"""
점프 투 파이썬 06장 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
만든이 : 김동현
만든 날짜 : 2021년 08월 13일 월요일
"""
sum = 0

for i in range(3, 1000):
    if i % 3 == 0 or i % 5 == 0:
            sum += i

print(sum)