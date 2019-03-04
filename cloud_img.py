# -*- coding:utf-8 -*-
#author:云亦然
#个性签名云图
#需自行安装jieba（pip install jieba）
#需自行安装matplotlib（pip install matplotlib）
#需自行安装wordcloud（pip install wordcloud）
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS

#获取个性签名
signatures = []
with open('WeChat_friends.txt',mode='r',encoding='utf-8') as b:
    rows = b.readlines()
    for row in rows:
        signature = row.split(',')[9]
        if signature != '':
            signatures.append(signature)

# 获取备注名
remarkNames = []
with open('WeChat_friends.txt', mode='r', encoding='utf-8') as b:
    rows = b.readlines()

    for row in rows:

        remarkName = row.split(',')[4]
        remarkName.replace('a.', 'span')
        if remarkName != '':

            remarkNames.append(remarkName)

#设置分词
split = jieba.cut_for_search(str(signatures))#搜索引擎模式，还有False精准模式分词，True全模式分词
split1 = jieba.cut_for_search(str(remarkNames))
words = ' '.join(split)#以空格进行拼接
words1 = ' '.join(split1)
#print(words)


#设置屏蔽词，去掉表情和特殊符号等
#图片生成的一些无法显示的表情都可以自行添加屏蔽
stopwords = STOPWORDS.copy()
stopwords.add('span')
stopwords.add('class')
stopwords.add('emoji')
stopwords.add('emoji1f334')
stopwords.add('emoji1f388')
stopwords.add('emoji1f338')
stopwords.add('emoji1f33a')
stopwords.add('emoji1f33c')
stopwords.add('emoji1f633')
stopwords.add('emoji2747')
stopwords.add('emoji2764')
stopwords.add('emoji1f4b5')
stopwords.add('emoji1f497')
stopwords.add('u200b')
stopwords.add("u200b'")

#导入背景图
bg_image = plt.imread('bg.jpg')
# 设置词云参数，参数分别表示：画布宽高、背景颜色、背景图形状、字体、屏蔽词、最大词的字体大小
wc = WordCloud(width=1024,height=768,background_color='white', mask=bg_image, font_path='simkai.ttf',
               stopwords=stopwords, max_font_size=400, random_state=50)
#simkai.ttf是系统的简体字体文件 在C:\Windows\Fonts目录下有

#将分词后的数据传入云图
wc.generate_from_text(words)
plt.imshow(wc) #绘制图像
plt.axis('off') #不显示坐标轴
#保存生成的图片
wc.to_file('个性签名云图.jpg')

wc.generate_from_text(words1)
plt.imshow(wc)
plt.axis('off')
wc.to_file('备注名云图.jpg')