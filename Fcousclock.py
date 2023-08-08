import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes, seconds = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# 设置专注时钟的分钟数
focus_minutes = 25

# 启动专注时钟
focus_timer(focus_minutes)
