import requests
import json


def is_network_available(url='https://www.baidu.com', timeout=3):
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

def get_config():
    with open("./config.json", "r", encoding="utf-8") as f:
        config = json.loads(f.read())
    return config


def qxwx_push(config):
    print("企业微信应用消息推送开始")
    qywx_corpid = config.get("qywx_corpid")
    qywx_agentid = config.get("qywx_agentid")
    qywx_corpsecret = config.get("qywx_corpsecret")
    qywx_touser = config.get("qywx_touser")
    res = requests.get(
        f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={qywx_corpid}&corpsecret={qywx_corpsecret}"
    )
    token = res.json().get("access_token", False)
    data = {
        "touser": qywx_touser,
        "agentid": int(qywx_agentid),
        "msgtype": "text",
        "text": {
            "content": f"Telecom Reconnect Done\n",
        },
    }
    res = requests.post(
        url=f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}",
        data=json.dumps(data),
    )
    res = res.json()
    if res.get("errcode") == 0:
        print("企业微信应用消息推送成功")
    else:
        print("企业微信应用消息推送失败")


if __name__ == "__main__":
    # config = get_config()
    # print(config)
    # if config.get("push"):
    #     qxwx_push(config.get("push_config"))
    print(is_network_available())
