# -*- coding:utf-8 -*-
#author:云亦然
#头像分析、拼接
#自行安装PIL和math（pip install Pillow）
import itchat
import os
import TencentYoutuyun
from pyecharts import Pie
from math import sqrt
from PIL import Image
# 获取微信好友头像
def get_head_image():
    a = 0
    itchat.auto_login()
    friends = itchat.get_friends(update=True)

    # 在当前位置创建一个存储头像的目录
    save_path = "head_images"
    if not os.path.exists(save_path):
        os.mkdir(save_path)


    #获取所以好友的头像,保存到本地
    for friend in friends:
        head = itchat.get_head_img(userName=friend['UserName'])
        img_name = friend['RemarkName']
        img_name = img_name.replace('"','')#把特殊符号"替换掉
        img_name = img_name.replace('.','')#把特殊符号.替换掉
        img_file = open(save_path + '/'+ img_name + '.jpg','wb')
        a+=1
        img_file.write(head)
        img_file.close()
        print(a)#输出遍历好友次数

def analyse_data():

    appid = '10170264'
    secret_id = 'AKIDrCQWnaxEMMDwKK4oNqnbSYihUWPuNdLz'
    secret_key = 'ayDXhF9tUzOfQTOzQtOpDeGayEJI7nJh'
    userid = '531845432'

    end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT  # 优图开放平台
    youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

    use_face = 0
    not_use_face = 0

    save_path = "head_images"
    for file_name in os.listdir(save_path):
        result = youtu.DetectFace(os.path.join(save_path, file_name))  # 人脸检测与分析
        # print(result)  # 参考 https://open.youtu.qq.com/legency/#/develop/api-face-analysis-detect
        # 判断是否使用人像
        if result['errorcode'] == 0:  # errorcode为0表示图片中存在人像
            use_face += 1
            gender = '男' if result['face'][0]['gender'] >= 50 else '女'
            age = result['face'][0]['age']
            beauty = result['face'][0]['beauty']  # 魅力值
            glasses = '不戴眼镜 ' if result['face'][0]['glasses'] == 0 else '戴眼镜'
            # print(file_name[:-4], gender, age, beauty, glasses, sep=',')
            with open('header.txt', mode='a', encoding='utf-8') as f:
                f.write('%s,%s,%d,%d,%s\n' % (file_name[:-4], gender, age, beauty, glasses))
        else:
            not_use_face += 1

    attr = ['使用人脸头像', '未使用人脸头像']
    value = [use_face, not_use_face]
    pie = Pie('好友头像分析', '', title_pos='center')
    pie.add('', attr, value, radius=[30, 75], is_label_show=True,is_legend_show=True, legend_top='bottom')
    # pie.show_config()
    pie.render('好友头像分析.html')





#拼接头像
def spliced_head(save_path):

    path_list = []
    for item in os.listdir(save_path):
        img_path = os.path.join(save_path,item)
        path_list.append(img_path)

        line = int(sqrt(len(path_list)))

        New_Image = Image.new('RGB',(128 * line,128 * line))

        x,y = 0,0
        for item in path_list:
            try:
                img = Image.open(item)
                img = img.resize((128,128),Image.ANTIALIAS)
                New_Image.paste(img,(x * 128,y * 128))
                x+=1
                print(x)#查看拼接进度
            except IOError:
                print("第%d行，%d列文件读取失败！IOError:%s"%(y,x,item))
            if x == line:
                x = 0
                y+=1
            if(x + line * y) == line * line:
                break

    New_Image.save('Avatarcollection.jpg')
    itchat.send_file('Avatarcollection.jpg', toUserName='filehelper')#发送头像合集到文件传输助手


if __name__ == '__main__':
    get_head_image()
    analyse_data()
    spliced_head("head_images")

