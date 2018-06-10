# -*- coding:utf-8 -*-

import os
import re
import subprocess
import sys

device = input("小燕请输入设备id：")

print("设备为：", device)
print("开始Push：")
os.system('adb -s %s push monkey.jar /sdcard/' %(device))
os.system('adb -s %s push framework.jar /sdcard/' %(device))
os.system('adb -s %s push max.xpath.actions /sdcard/' %(device))
os.system('adb -s %s push max.xpath.selector /sdcard/' %(device))
os.system('adb -s %s push max.widget.black /sdcard/' %(device))
os.system('adb -s %s push max.config /sdcard/' %(device))
os.system('adb -s %s push leak_upload.config /sdcard/' %(device))
print("完成Push:")

print('开始执行monkey')
os.system('adb -s %s shell CLASSPATH=/sdcard/monkey.jar:/sdcard/framework.jar exec app_process /system/bin tv.panda.test.monkey.Monkey -p com.sina.weibo --uiautomatormix --running-minutes 100 -v -v' %(device))
print('完成执行monkey')
print('开始拷贝日志')
os.system('adb -s %s pull /sdcard/crash-dump.log  test_result' %(device))
os.system('adb -s %s pull /sdcard/sina/weibo/crash.log test_result' %(device))
os.system('adb -s %s pull /data/anr/traces.txt test_result' %(device))
try:
    os.rename('test_result/crash-dump.log', 'test_result/%s_crash-dump.log' %(device))
except OSError as e:
    print("重命名crash-dump.log出错", e)

try:   
    os.rename('test_result/crash.log.log', 'test_result/%s_crash.log' %(device))
except OSError as e:
    print("重命名crash.log日志出错", e)

try:
    os.rename('test_result/traces.txt', 'test_result/%s_traces.txt' %(device))
except OSError as e:
    print("重命名traces.txt出错", e)

print('完成拷贝日志')



# for device in devices:
#     print("设备：", device)
#     print("开始Push：")
#     os.system('adb -s %s push monkey.jar /sdcard' %(device))
#     os.system('adb -s %s push framework.jar /sdcard' %(device))
#     os.system('adb -s %s push max.xpath.actions /sdcard' %(device))
#     os.system('adb -s %s push max.xpath.selector /sdcard' %(device))
#     os.system('adb -s %s push max.widget.black /sdcard' %(device))
#     os.system('adb -s %s push max.config /sdcard' %(device))
#     os.system('adb -s %s push leak_upload.config /sdcard' %(device))
#     print("完成Push:")

#     print('开始执行monkey')
#     os.system('adb -s %s shell CLASSPATH=/sdcard/monkey.jar:/sdcard/framework.jar exec app_process /system/bin tv.panda.test.monkey.Monkey -p com.sina.weibo --uiautomatormix --running-minutes 100 -v -v' %(device))
#     print('完成执行monkey')



