# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 9:19
# @Author  : ChangJun
# @Email   : 52chinaweb@gmail.com 
# @desc    : 实现微信机器人

import itchat
import requests


def get_response(msg):
    apiUrl = 'http://openapi.tuling123.com/openapi/api'
    data = {
        'key': '123',
        'info': msg,
        'userid': '52chinaweb'
    }
    result = requests.post(apiUrl, data=data).json()
    if msg == '高艳琪':
        result.update(text='高艳琪是世界上最美丽的女孩！')
    print('我的回复是:{0}'.format(result.get('text')))
    return result.get('text')


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print('我收到的消息:{0}'.format(msg['Text']))
    return get_response(msg['Text'])


itchat.auto_login(hotReload=True)
itchat.run()
