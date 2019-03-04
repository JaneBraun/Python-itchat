# -*- coding:utf-8 -*-
#author:云亦然
#需自行安装pyecharts（pip install pyecharts）
#用pyecharts制作图表 便于分析
#导入pie组件，生成饼图
from pyecharts import Pie


sex = [] #创建空列表,用来记录好友性别
with open('WeChat_friends.txt',mode='r',encoding='utf-8') as b:
    rows =b.readlines()
    for row in rows:
        sex.append(row.split(',')[5])

attr = ['男生','女生','不详']#性别分类
value = [sex.count('1'),sex.count('2'),sex.count('0')]

pie = Pie('微信好友性别比例','好友总人数:%d' %len(sex),title_pos="center")#绘制的标题在中间显示

pie.add('',attr,value,radius=[30,75],label_text_color=None,is_label_show=True,is_legend_orient="vertical",legend_pos="left")

# radius：扇区圆心角展现数据的百分比，半径展现数据的大小
# area：所有扇区圆心角相同，仅通过半径展现数据大小

pie.render('好友性别分析.html')
