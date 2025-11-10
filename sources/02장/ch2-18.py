"""프로그램 2.18: 문자열 메소드 strip(), split(), join()"""

msg= "   Hi, Kim   ".strip() 	    # 앞뒤에 붙은 공백 제거
print(msg)			    # 출력: 'Hi, Kim' 
data = "12:02:30".split(':') 	    # 인자를 기준으로 분리하여 만든 리스트를 반환
print(data)			    # 출력: ['12', '02', '30']
data = " 1 2  3   4".split()	    # 인자가 생략되면 공백을 기준으로 분리함
print(data)			    # 출력: ['1', '2', '3', '4']
names = ["kim", "lee", "park"]	    # 문자열 리스트
result = ''.join(names)		    # 문자열 요소들 합치기
print(result)			    # 출력: kimleepark
result = ', '.join(names)	    # 문자열 사이에 ', '를 넣어 합치기
print(result)			    # 출력: kim, lee, park
