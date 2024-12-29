from push_tool import is_network_available
from time import sleep
from reconnect import all_run
from push_tool import get_config, qxwx_push
import pyautogui
pyautogui.FAILSAFE = False

def check():
    network_flag = False
    check_time=3
    while not network_flag and check_time > 0:
        network_flag = is_network_available()
        if not network_flag:
            print(f"Network is not available, wait {check_time}sec and check again.")
            check_time -= 1
            sleep(1)
    if network_flag:
        print("Network is available.")
        push__config = get_config()
        if push__config.get("push"):
            qxwx_push(push__config.get("push_config"), "Network is available.")
    else:
        print("Network is not available.")
        all_run()

if __name__ == "__main__":
    check()
