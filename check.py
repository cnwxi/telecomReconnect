from push_tool import is_network_available
from time import sleep
from reconnect import all_run
from push_tool import get_config, qxwx_push, qqmail_push
import pyautogui

pyautogui.FAILSAFE = False


def check():
    network_flag = False
    check_time = 3  # 最多检测3次网络是否可用
    while not network_flag and check_time > 0:  # 检测网络是否可用
        network_flag = is_network_available()
        if not network_flag:
            print(f"Network is not available, wait {check_time}sec and check again.")
            check_time -= 1
            sleep(1)
    if network_flag:  # 网络可用
        print("Network is available.")
        push_config = get_config()
        if push_config.get("push"):  # 如果开启了推送
            if push_config.get("push_config").get("type") == "qywx":  # 企业微信推送
                qxwx_push(push_config.get("push_config"), "Network is available.")
            elif push_config.get("push_config").get("type") == "qqmail":  # QQ邮箱推送
                qqmail_push(push_config.get("push_config"), "Network is available.")
    else:  # 网络不可用
        print("Network is not available.")
        all_run()  # 网络不可用时执行重连操作


if __name__ == "__main__":
    check()
