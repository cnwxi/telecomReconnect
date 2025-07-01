import requests
import json


def is_network_available(url='http://connect.rom.miui.com/generate_204', timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        # print(response.status_code)
        return response.status_code == 204
    except requests.ConnectionError:
        return False


def get_config():
    with open("./config.json", "r", encoding="utf-8") as f:
        config = json.loads(f.read())
    return config


def qxwx_push(config, content):
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
            "content": content,
        },
    }
    res = requests.post(
        url=
        f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}",
        data=json.dumps(data),
    )
    res = res.json()
    if res.get("errcode") == 0:
        print("企业微信应用消息推送成功")
        return True
    else:
        print("企业微信应用消息推送失败")
        return False

def qqmail_push(config, content):
    print("QQ邮箱推送开始")
    qqmail_user = config.get("qqmail_user")
    qqmail_password = config.get("qqmail_password")
    qqmail_to = qqmail_user  # 默认发送到自己
    
    msg = MIMEText(f"{content}", 'plain', 'utf-8')
    msg['Subject'] = Header(f'网络检测/重连信息推送', 'utf-8')
    msg['From'] = qqmail_user
    msg['To'] = qqmail_to

    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(qqmail_user, qqmail_password)
        server.sendmail(qqmail_user, qqmail_to, msg.as_string())
        print("QQ邮箱推送成功")
    except Exception as e:
        print(f"QQ邮箱推送失败: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    # config = get_config()
    # print(config)
    # if config.get("push"):
    #     qxwx_push(config.get("push_config"))
    print(is_network_available())
