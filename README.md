# Python-itchat
Python-itchat之微信好友大曝光

itchat的项目简介：
https://itchat.readthedocs.io/zh/latest/

itchat是开源的微信个人号接口，可以在py2.7和py3.5的版本环境下运用

py的安装和环境搭建 自行百度哈

要想曝光前必须得安装itchat：

通过以下命令安装itchat：
pip install itchat

然后就是打开我们的IDE工具PyCharm（我个人用得比较多的是这款，其他的也行）,创建一个名为acuire.py的文件

以下是该文件的代码 
（请看文件）

保存好代码之后 就可以在命令行输入：python acquire.py 静候 出现一个二维码扫描登录 登录完成后  该文件下的目录就会生成一个WeChat_friends.txt的文件了。这文件里面就是我们微信好友全部的信息了

接下来就是对保存的数据进行分析了

我们继续创建一个analyze.py文件
在这之前，需要安装pyecharts，命令行输入:pip install pyecharts

文件的代码如下

（请看文件）




在运行python analyze.py时 有可能会出现No module named ‘pyechars_snapshot’的错误

解决方法是:
https://pypi.org/project/pyecharts-snapshot/#files
下载此文件后，在目录下打开cmd使用命令 pip install pyecharts_snapshot-0.1.8-py2.py3-none-any.whl 安装完成即可

然后你就会发现目录下生成了一个好友性别分析.html的文件 

打开就是如图所示了：


更多的小伙伴对这个图是很感应趣
：
是怎么做出来的呢 他可以是个性签名云图也可以是备注名云图

创建cloud_img.py文件，代码如下

（请看文件）
安装对应需要的库和把字体文件复制到当前目录下 即可 
命令行输入：python cloud_img.py 两张图片就出来了


接下来就是最精彩的部分了
头像分析和头像拼接
直接上效果图：


接下来就是准备部分了

需要用到腾讯优图的人脸识别，习惯性的用python中的
pip install TencentYoutuyun 结果失败了

正确方法：下载sdk文件：https://github.com/Tencent-YouTu/Python_sdk
打开下载目录 运行cmd 命令行输入pip install Python_sdk-master.zip

然后要到腾讯忧图（https://open.youtu.qq.com/）申请公有云服务 （我是一天内就申请到了，就说是运用python-itchat的获取头像后 比对头像是否是真人头像的一次测试）
然后我们申请成功后就会有AppID SecretID SecreKey 三个参数。
接着我们就创建head_portrait.py
代码如下：
（请看文件）



然后如果联系人比较多的话 拼接是需要点时间的 
微信好友大曝光到此结束！
