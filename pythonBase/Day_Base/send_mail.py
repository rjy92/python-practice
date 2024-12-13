# 日报：每天早上9点发昨日关键指标的情况
# 昨日招生：130人 环比前日 20%，本周累计，本月累计
# 人工智能：20人 环比前日 20%
# 数据分析：10人 环比前日 20%
# 人工
# 1. 每天早上到crm系统中（数据库，前端）获取本月报名信息
#    pytyon 连数据库——后边讲sql
# 2. 总量统计，分学科统计
#    pytyon对数据进行统计
# 3. 日报信息发给领导(社交群,邮件)
import yagmail
#     1.到邮件服务器登录邮箱
yagmial_server=yagmail.SMTP(host="smtp.163.com",
                            user="guxiaoyan003@163.com",
                            password="RZCRLEUXEVBNETKX")
#python登录邮箱属于第三方登录，所以不能用正常的密码，要用授权码
#     2.写邮件（收件人，标题，内容）
to_user="253128713@qq.com" #收件人，可给容器实现发送给多人
chaosong="" #抄送人 ，可给容器实现抄送给多人
title="日报" #标题
con = "测试日报" #内容
#     3.发送
yagmial_server.send(to_user,title,con)

#定时执行此python文件
# 命令行执行如下指令 文件路径不要有中文:
# python  D:\pythonProject\Day_01\send_mail.py
#
# #提示 no  module name "yagmail“时，重新安装此模块
# pip install yagmial
#
# 建立一个文本文件，并把扩展名.txt 改为 .bat
# 文件内容 为
# @python  'D:/pythonProject/Day_01/send_mail.py'
# 双击此.bat文件（查看是否正常发邮件)

#做定时执行.bat文件
# 任务栏：搜索 “任务计划程序”.右侧新建任务
#   常规：名字
#   触发器:一次，开始时间，结束时间，重复任务间隔2分钟
#   操作：新建——选bat文件
#
# pip 安装包（后序课程要用)
# import 3种导入方法





