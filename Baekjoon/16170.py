# 16170 오늘의 날짜는?
from datetime import datetime
if __name__ == "__main__":
    now = datetime.now()
    print(now.year)
    print(now.month)
    print(now.day)