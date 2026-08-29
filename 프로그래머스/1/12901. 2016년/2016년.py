import datetime

def solution(a, b):
    answer = ''
    target_date = datetime.date(2016, a, b).weekday()
    days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return days[target_date]