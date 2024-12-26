# -*- coding: utf-8 -*-

from time import sleep
import pyautogui
from push_tool import get_config, qxwx_push, is_network_available
pyautogui.FAILSAFE = False


def awake_windows():
    pyautogui.click(1910, 10, 2)
    sleep(2)
    pyautogui.click(0, 10, 2)
    sleep(2)


def open_telecom():
    pyautogui.click(1655, 1055)
    sleep(1)


def reconnect_telecom():
    # 断开
    pyautogui.click(960, 600)
    sleep(10)
    # 登录
    pyautogui.click(960, 555)
    sleep(10)
    pyautogui.click(1910, 10)


def close_telecom():
    pyautogui.click(1110, 255)
    print("Reconnect done!")
    sleep(1)


def countdown(seconds):
    while seconds:
        pyautogui.click(seconds % 2 * 1910, 10)  # 防止屏保
        mins, secs = divmod(seconds, 60)
        timeformat = "Checking network, please wait... {:02d}:{:02d}".format(mins, secs)
        if not is_network_available():
            return False
        print(timeformat, end="\r")  # 使用 '\r' 来覆盖同一行的内容
        sleep(1)
        seconds -= 1
    print("Time's up!")
    return True


def reconnect():
    print("Start reconnect.")
    network_flag = False
    wait_time = 60
    while not network_flag:
        # reconnect
        reconnect_telecom()
        # wait for check network
        print(f"Wait {wait_time}sec and check network")
        network_flag = countdown(wait_time)
        # check network
        if network_flag:
            config = get_config()
            if config.get("push"):
                push_flag=False
                push_times = 0
                while not push_flag and push_times < 3:
                    try:
                        push_flag = qxwx_push(config.get("push_config"))
                    except:
                        sleep(1)
                    push_times += 1
        else:
            print("\nNetwork error.Reconnecting...")

def all_run():
    awake_windows()
    open_telecom()
    reconnect()
    close_telecom()

if __name__ == "__main__":
    awake_windows()
    all_run()
