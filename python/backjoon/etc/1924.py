import datetime

n, m = map(int, input().split())
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
day = datetime.date(2007, n, m).weekday()

print(days[day])
