#!/usr/bin/env python3


import requests
from dotenv import load_dotenv

import myconfig
import notify

# 一开始在浏览器抓了半天请求，把访问过程理清楚，写成脚本以后发现密码错误，似乎没有办法处理特殊字符
# 于是我准备把密码修改成简单一点的，然后发现用户设置里有API可以调用，完全不用搞这么麻烦 😅

checkin_url = "https://api.sockboom.click/client/checkin"


def checkin():
    params = {"token": myconfig.SOCKBOOM_KEY}
    response = requests.get(
        url=checkin_url,
        params=params,
    )
    checkin_status = response.json()
    if checkin_status["success"] == 1:
        traffic = checkin_status["traffic"]
        traffic = round(float(traffic) / 8 / 1024 / 1024)
        notify.send("sockboom签到成功", f"获得流量{traffic}MB")
    elif checkin_status["success"] == 0:
        notify.send("sockboom已签到", "无须重复签到")
    else:
        notify.send("sockboom签到失败", "api key错误")


def main():
    load_dotenv()
    if not myconfig.SOCKBOOM_KEY:
        notify.send("未找到SOCKBOOM配置", "请先在配置文件配置api key")
    else:
        checkin()


if __name__ == "__main__":
    main()
