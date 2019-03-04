# -*- coding:utf-8 -*-
#author:云亦然
#需自行安装itchat（pip install itchat）
#导入itchat模块，在网页版上操作微信账号的接口
import itchat

#获取微信的数据
def acquire_data():
    #扫描二维码，登录微信
    itchat.auto_login()
    #获取所有好友信息
    friends = itchat.get_friends(update=True) #返回用户信息字典
    return friends

#处理微信的数据
def parse_data(data):
    friends = []
    for item in data[1:]: #第一个元素是自己排除掉
        friend = {
            'UserName':item['UserName'],#微信系统内的用户编码标识
            'DisplayName':item['DisplayName'],#好友微信名
            'NickName':item['NickName'],#好友昵称
            'HeadImgUrl':item['HeadImgUrl'],#微信系统内的头像URL
            'RemarkName':item['RemarkName'],#好友备注名
            'Sex':item['Sex'],#性别 1为男2为女0未设置
            'Province':item['Province'],#省份
            'City':item['City'],#城市
            'Alias':item['Alias'],#微信号
            'Signature':item['Signature'].replace('\n','').replace(',',''),#个性签名（replace替换掉内容换行和逗号）
            'StarFriend':item['StarFriend'],#星标好友：1是0否
            'ContactFlag':item['ContactFlag'],#好友类型权限：：1和3好友，259和33027不让他看我的朋友圈，65539不看他的朋友圈，65795两项设置全禁止
        }
        friends.append(friend)
    return friends

#存储数据，存储到txt文件上
def save_data():
    friends = parse_data(acquire_data())#把返回的字典用处理函数处理
    for item in friends:
        with open('WeChat_friends.txt',mode='a',encoding='utf-8') as b:
            b.write('%s,%s,%s,%s,%s,%d,%s,%s,%s,%s,%d,%d\n' %(item['UserName'],item['DisplayName'],item['NickName'],
                                                              item['HeadImgUrl'],item['RemarkName'],item['Sex'],
                                                              item['Province'],item['City'],item['Alias'],item['Signature'],
                                                              item['StarFriend'],item['ContactFlag']))

if __name__ == '__main__':
    save_data()