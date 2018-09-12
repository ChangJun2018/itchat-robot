# -*- coding: utf-8 -*-
# @Time    : 2018/9/12 9:47
# @Author  : ChangJun
# @Email   : 52chinaweb@gmail.com 
# @desc    : 实现微信群发

import itchat, time

itchat.auto_login(True)

SINCERE_WISH = '你好'

friendList = itchat.get_friends(update=True)[1:]
for friend in friendList:
    itchat.send(SINCERE_WISH % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
    time.sleep(.5)
