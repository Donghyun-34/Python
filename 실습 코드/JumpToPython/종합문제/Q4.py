"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 14일 화요일
내용 : 리스트 총합 구하기
"""
score = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for i in score:
    if i >= 50:
        sum += i
print(sum)