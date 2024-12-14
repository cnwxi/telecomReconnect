import requests
import json


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
            "content": f"电信校园网自动登录\n",
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
    config = get_config()
    print(config)
    if config.get("push"):
        qxwx_push(config.get("push_config"))
    
