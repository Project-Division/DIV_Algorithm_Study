from datetime import datetime

# 현재 날짜와 시간 로드
today = datetime.today()

# 날짜를 "년-월-일" 형식으로 출력
print(today.strftime("%Y-%m-%d"))
