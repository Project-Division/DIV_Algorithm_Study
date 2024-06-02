import calendar as cd

List = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
x, y = map(int,input().split())

day = cd.weekday(2007, x, y)
print(List[Day])
