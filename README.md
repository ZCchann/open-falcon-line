# open-falcon-line

将open-falcon alarm组件的报警信息推送至line bot

**使用前请先修改mysql 中 uic库中的user表，把im字段的大小改为4000(line bot token较长 需要更改长度防止溢出)**

### open-falcon的设置



### 创建一个line bot

创建bot可以参照这篇文章  https://www.oxxostudio.tw/articles/201701/line-bot.html 

复制创建好的机器人的Channel Access Token 到open-falcon的dashboard页面上创建一个用户账号 在im部分填入Token即可



### 发送报警至个人

默认机器人报警只能发送给机器人的创建者，在创建机器人的页面可以查询到创建者的**user id**

复制**user id** 修改seting.json内的"master_userID"字段 将网页上的**user id**填入即可

随后启动脚本即可测试报警推送

### 发送报警至群组

群组id获取功能开发中

当前若需要获取群组id可以使用官方的line_bot_sdk创建一个api脚本 然后将机器人拉入群组内 发送任意消息查看群组ID

![](https://github.com/ZCchann/open-falcon-line/blob/master/README.assets/group_id.png)

随后将群组ID填入seting.json内的"master_userID"字段即可推送报警测试

### 消息格式

**当前推送消息格式如下**

状态异常
报警主机： zc-test
错误信息 :agent掉线
报警数值: agent.alive -1<1
报警时间: 2019-12-22 00:30:00 
