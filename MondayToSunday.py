'''得到每周的日期输出'''
from datetime import datetime, timedelta

def get_week_range(year, month, day):
    # 获取给定日期所在周的周一和周日的日期
    date = datetime(year, month, day)
    monday = date - timedelta(days=date.weekday())
    sunday = monday + timedelta(days=6)
    return monday, sunday

# 2024年的第一周开始日期
start_date = datetime(2024, 1, 1)

# 遍历2024年的每一周
while start_date.year == 2024:
    # 获取本周的日期范围
    monday, sunday = get_week_range(start_date.year, start_date.month, start_date.day)
    # 打印日期范围，并添加"周报"两字
    print(f"{monday.strftime('%Y.%m.%d')}-{sunday.strftime('%Y.%m.%d')}周报")
    # 下一周的开始日期
    start_date += timedelta(weeks=1)
