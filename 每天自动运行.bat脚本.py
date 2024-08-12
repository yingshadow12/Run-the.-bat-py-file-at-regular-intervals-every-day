import schedule
import time
import subprocess

def run_bat_file():
    subprocess.run([r"C:\myszdqd\MihoyoBBSTools-master\&python main_multi.py autorun.bat"], shell=True)

# 每天20点执行一次 修改20:00修改自动时间
schedule.every().day.at("20:00").do(run_bat_file)

while True:
    schedule.run_pending()
    time.sleep(1)
