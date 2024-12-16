# -*- coding: utf-8 -*-

from time import sleep
import pyautogui
from push_tool import get_config, qxwx_push, is_network_available

pyautogui.FAILSAFE = False


def click_press():
    pyautogui.click(1910, 10, 2)
    pyautogui.click(1910, 10, 2)
    print("start reconnect mission")
    sleep(3)
    # pyautogui.press("win")
    # 工具
    # pyautogui.moveTo(720, 640)
    # sleep(1)
    # pyautogui.click()
    # 天翼校园
    pyautogui.moveTo(1655, 1055)
    sleep(1)
    pyautogui.click()
    # 断开
    pyautogui.moveTo(960, 600)
    sleep(1)
    pyautogui.click()
    # 登录
    pyautogui.moveTo(960, 555)
    sleep(5)
    pyautogui.click()
    # 关闭
    pyautogui.moveTo(1110, 255)
    sleep(3)
    pyautogui.click()
    # 留空时间，等待网络连接
    sleep(5)


def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        if not is_network_available():
            return False
        print(timeformat, end='\r')  # 使用 '\r' 来覆盖同一行的内容
        sleep(1)
        seconds -= 1
    print("Time's up!")
    return True

def reconnect():
    network_flag = False
    while not network_flag:
        # reconnect
        click_press()
        # wait 60s
        print("wait 60sec and check network")
        network_flag = countdown(60)
        # check network
        if network_flag:
            config = get_config()
            if config.get("push"):
                qxwx_push(config.get("push_config"))
        else:
            print('network error.')


if __name__ == "__main__":
    reconnect()
