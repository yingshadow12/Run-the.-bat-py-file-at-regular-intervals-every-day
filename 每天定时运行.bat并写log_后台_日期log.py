import schedule
import time
import subprocess
from datetime import datetime
import os


def run_bat_file():
    # 生成日志文件名称，按照“年-月-日”格式
    log_file_name = f"{datetime.now().strftime('%Y-%m-%d')}.log.txt"
    log_file_path = log_file_name

    try:
        # 打开日志文件追加模式
        with open(log_file_path, "a") as log_file:
            # 写入当前时间和开始运行的消息，格式化时间为不含微秒
            log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: 正在运行批处理文件...\n")

            # 执行批处理文件，并将输出和错误重定向到日志文件
            result = subprocess.run(
                [r"C:your.bat"],
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # 将标准输出写入日志文件
            log_file.write(result.stdout)

            # 将标准错误写入日志文件
            if result.stderr:
                log_file.write(result.stderr)

            log_file.write(f"\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: 批处理文件已成功执行.\n\n\n")
    except Exception as e:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: 发生错误 - {e}\n\n\n")


# 每天7点执行一次 修改07:00更改执行时间
schedule.every().day.at("07:00").do(run_bat_file)


# 后台运行脚本
def background_task():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    # 在后台运行
    if os.name == 'nt':
        import ctypes

        whnd = ctypes.windll.kernel32.GetConsoleWindow()
        if whnd != 0:
            ctypes.windll.user32.ShowWindow(whnd, 0)
            ctypes.windll.kernel32.CloseHandle(whnd)
    background_task()
