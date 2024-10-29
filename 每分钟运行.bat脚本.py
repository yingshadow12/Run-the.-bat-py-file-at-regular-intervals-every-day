import time
import subprocess

def run_bat_file():
    subprocess.run([r"C:\your bat.bat"], shell=True)
    time.sleep(2)  # 因为以秒定时，所以暂停2秒，使之不会在1秒内执行多次

while True:
    time_now = time.strftime("%S", time.localtime())  # 刷新时间，获取当前秒数
    if time_now == "10":  # 每天定时的时间，这里设置为每分钟的第10秒执行
        run_bat_file()  # 执行需要定时执行的动作
