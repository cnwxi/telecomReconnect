# -*- coding: utf-8 -*-

from time import sleep
import pyautogui
from push_tool import get_config, qxwx_push, is_network_available, qqmail_push

pyautogui.FAILSAFE = False


def awake_windows():  # 唤醒屏幕 右上角空白位置 1080p屏幕 具体位置可使用mouse_listen.py脚本获取
    pyautogui.click(1910, 10, 2) # mouse_listen.py
    sleep(2)
    pyautogui.click(1910, 10, 2) # mouse_listen.py
    sleep(3)


def open_telecom():  # 打开电信宽带登录界面
    pyautogui.click(1673, 1055) # mouse_listen.py
    sleep(1)


def reconnect_telecom():  # 重连电信宽带
    # 断开
    pyautogui.click(960, 600) # mouse_listen.py
    sleep(10)
    # 登录
    pyautogui.click(960, 555) # mouse_listen.py
    sleep(10)
    pyautogui.click(1910, 10) # mouse_listen.py 移开鼠标进入下一事件


def close_telecom():  # 关闭电信宽带登录界面
    pyautogui.click(1110, 255) # mouse_listen.py
    print("Reconnect done!")
    sleep(1)


def countdown(seconds):  # 倒计时函数，检测网络是否可用
    while seconds:
        pyautogui.click(1910, 10)   # mouse_listen.py 防止屏保 
        mins, secs = divmod(seconds, 60)
        timeformat = "Checking network, please wait... {:02d}:{:02d}".format(mins, secs)
        if not is_network_available():
            return False
        print(timeformat, end="\r")  # 使用 '\r' 来覆盖同一行的内容
        sleep(1)
        seconds -= 1
    print("Time's up!")
    return True


def reconnect():  # 重连操作
    print("Start reconnect.")
    network_flag = False
    wait_time = 60
    while not network_flag:  # 网络不可用，重复循环
        # reconnect
        reconnect_telecom()  # 重连电信宽带
        # wait for check network
        print(f"Wait {wait_time}sec and check network")
        network_flag = countdown(wait_time)  # 检测网络是否可用
        # check network
        if network_flag:  # 网络可用
            config = get_config()  # 获取推送配置
            if config.get("push"):  # 如果开启了推送
                push_flag = False
                push_times = 0
                while not push_flag and push_times < 3:  # 推送失败最多重试3次
                    try:
                        if (
                            config.get("push_config").get("type") == "qywx"
                        ):  # 企业微信推送
                            push_flag = qxwx_push(
                                config.get("push_config"), "Reconnect successfully!"
                            )
                        elif (
                            config.get("push_config").get("type") == "qqmail"
                        ):  # QQ邮箱推送
                            push_flag = qqmail_push(
                                config.get("push_config"), "Reconnect successfully!"
                            )
                    except:
                        sleep(1)
                    push_times += 1
        else:  # 网络不可用，输出信息
            print("\nNetwork error.Reconnecting...")


def all_run():
    awake_windows()
    awake_windows()
    open_telecom()
    reconnect()
    close_telecom()


if __name__ == "__main__":
    all_run()
