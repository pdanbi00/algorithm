from datetime import datetime
months = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
D, M = map(int, input().split())
print(months[datetime(year=2009, month=M, day=D).weekday()])