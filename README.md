# wechat_ticket
微信前沿讲座抢票小程序V1.0

需要环境：
python2.7 + requests。

使用说明：

1.点击阅读原文后，获取url网址。例如：https://u9hb4f.fanqier.com/f/xtz4fk

2.在Chorme或者火狐浏览浏览器中打开这个网址；

3.在地址栏中添加一个字段‘/readonly’，形如：https://u9hb4f.fanqier.com/f/xtz4fk/readonly  摁下回车键；

4.打开调试工具（摁F12），刷新页面。在Network（火狐的话是网络标签）标签下，找到xtz4fk?force=true，并点击查看响应。

5.在返回数据的data中，找到_id键的值。并把这个值复制到程序中的formId，并且程序中请求的url的地址的最后一串数字，也改为这个键的值。

6.在data.items中一般是四个对象。

7.在data.items[0]中，找到_id键的值，并复制到程序中obj对象中的definition的值。

8.在data.items[1]中，查看lable值是否为“姓名”，是的话，把_id键的值赋值给程序中name对象的definition，并且修改value值为你的名字。

9.在data.items[2]中，查看lable值是否为“学号”，是的话，把_id键的值赋值给程序中card对象的definition，并且修改value值为你的学号。

10.在data.items[3]中，查看lable值是否为“手机”，是的话，同样把_id键的值赋值给程序中phone对象的definition，并且修改value值为你的手机号。

11.保存程序。

12.运行程序。python wechat_finallyV2.py。然后输入数字1就可以开始刷票了。

# 注意：

程序默认是1秒提交一次。

最好等到还有30秒的时候，摁数字1，不然的话，过早提交的话，服务器会暂时不处理我们发起请求，导致无法抢票！！！


喜欢的话，不要忘记点击Star哦。
