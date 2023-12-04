import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"剩余时间：{seconds // 60} 分钟 {seconds % 60} 秒")
        time.sleep(1)
        seconds -= 1
    print("时间到！")

# 设置专注时长为 25 分钟
focus_timer(25)
