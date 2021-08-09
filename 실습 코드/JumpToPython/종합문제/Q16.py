"""
점프 투 파이썬 종합문제
만든이 : 김동현
만든 날짜 : 2020년 07월 14일 화요일
내용 : 모스 부호 해독 -> 딕셔너리와 메타 문자 활용
"""
dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

morse = input()
res = []

for word in morse.split("  "): # 주어진 문장을 단어 단위로 구분
    for char in word.split(" "): # 단어를 문자 단위로 구분
        res.append(dic[char])
    res.append(" ")

print("".join(res))