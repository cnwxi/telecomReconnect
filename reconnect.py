from time import sleep
import pyautogui
from push_tool import get_config, qxwx_push

pyautogui.FAILSAFE = False


def reconnect():
    pyautogui.click(1910, 10, 2)
    print("start reconnect mission")
    sleep(3)
    pyautogui.press("win")
    # pyautogui.moveTo()
    # 工具
    pyautogui.moveTo(720, 640)
    sleep(1)
    pyautogui.click()
    # 天翼校园
    pyautogui.moveTo(815, 615)
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
    sleep(3)
    config=get_config()
    if config.get("push"):
        qxwx_push(config.get("push_config"))


if __name__ == "__main__":
    reconnect()
