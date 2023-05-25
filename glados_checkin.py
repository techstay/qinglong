#!/usr/bin/env python3

import json
from typing import Dict

import requests
from dotenv import load_dotenv

import myconfig
import notify

checkin_url = 'https://glados.rocks/api/user/checkin'
checkin_status_url = 'https://glados.rocks/api/user/status'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
payload = {"token": "glados.network"}
headers = {
    'origin': 'https://glados.rocks',
    'user-agent': user_agent,
    'content-type': 'application/json;charset=UTF-8',
}


def checkin(cookie: Dict[str, str]) -> None:
    try:
        checkin_result = requests.post(
            url=checkin_url,
            headers=headers,
            cookies=cookie,
            data=json.dumps(payload),
        ).json()

        checkin_status = requests.get(
            url=checkin_status_url,
            headers=headers,
            cookies=cookie,
        ).json()

        email = checkin_status['data']['email']
        left_days = round(float(checkin_status['data']['leftDays']))

        if checkin_result['code'] == 0:
            notify.send(
                'glados签到成功',
                f"账号{email}, 剩余时长{left_days}天",
            )
        elif checkin_result['code'] == 1:
            message = checkin_result['message']
            notify.send(
                f'glados已签到:{message}',
                f"账号{email}, 剩余时长{left_days}天",
            )
        else:
            raise Exception(checkin_result)
    except Exception as e:
        notify.send('glados签到失败，请检查错误提示', e)


def main():
    load_dotenv()
    if len(myconfig.GLADOS_COOKIES) == 0:
        notify.send('glados未找到配置', '请先在配置文件中设置你的glados cookie')
        exit(1)

    for cookie in myconfig.GLADOS_COOKIES:
        checkin(cookie)


if __name__ == '__main__':
    main()
