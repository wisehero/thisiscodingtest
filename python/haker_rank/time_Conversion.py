def timeConversion(s):
    # s가 PM이라면 24시간 표기법으로 바꿔서 출력하고
    if s[8:len(s)] == "PM":
        if int(s[:2]) < 12:
            s = str(int(s[:2]) + 12) + s[2:8]
        else:
            return s
    else:
        # AM이라면 12시간 표기법으로 바꿔서 출력해야 한다.
        return str(int(s[:2]) - 12) + s[2:8]
    print(s)



timeConversion("07:05:45PM")
