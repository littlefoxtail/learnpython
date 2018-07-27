# -*- coding:utf-8 -*-

import os
import re
import time
import subprocess


def get_devices(adb_path='adb'):
    with open(os.devnull, 'wb') as devnull:
        subprocess.check_call([adb_path, 'start-server'], stdout=devnull,
                              stderr=devnull)
    out = split_lines(
        subprocess.check_output([adb_path, 'devices']).decode('utf-8'))
    devices = []
    for line in out[1:]:
        if not line.strip():
            continue
        if 'offline' in line:
            continue
        serial, _ = re.split(r'\s+', line, maxsplit=1)
        devices.append(serial)
    return devices

def split_lines(s):
    """Splits lines in a way that works even on Windows and old devices.
    Windows will see \r\n instead of \n, old devices do the same, old devices
    on Windows will see \r\r\n.
    """
    return re.split(r'[\r\n]+', s.rstrip())
devices = get_devices()

for device in devices:    
    model = subprocess.check_output(['adb','-s', device, 'shell', 'getprop', 'ro.product.model']).decode('utf-8')
    mode2 = model.replace(" ", "_")
    print("本次跑的设备是",mode2)
    name= device+'_'+mode2
    print("名字好了",name)
    print("设备ID：",device)
    print("开始Push：")
    
##    os.system('adb -s %s push monkey.jar /sdcard/' %(device))
##    os.system('adb -s %s push framework.jar /sdcard/' %(device))
##    os.system('adb -s %s push max.xpath.actions /sdcard/' %(device))
##    os.system('adb -s %s push max.xpath.selector /sdcard/' %(device))
##    os.system('adb -s %s push max.widget.black /sdcard/' %(device))
##    os.system('adb -s %s push max.config /sdcard/' %(device))
    print("完成Push:")
    print("test_result/%s" %(name))

    current_path = os.path.abspath(os.path.dirname(__file__))
    folder = '%s/test_result/%s/' %(current_path, model)
    exists  = os.path.exists(folder)
    if not exists:
        os.makedirs(folder)
    time.sleep(10)
    print('目录创建成功')
    time.sleep(10)
    print('开始执行monkey')
   #  os.system('adb -s %s shell CLASSPATH=/sdcard/monkey.jar:/sdcard/framework.jar exec app_process /system/bin tv.panda.test.monkey.Monkey -p com.sina.weibo --uiautomatormix --running-minutes 3 -v -v' %(device))
    print('完成执行monkey')
    print('开始拷贝日志')
    os.system('adb -s %s pull /sdcard/crash-dump.log  test_result/%s' %(device,name))
    os.system('adb -s %s pull /sdcard/sina/weibo/crash.log test_result/%s' %(device,name))
    os.system('adb -s %s pull /data/anr/traces.txt test_result/%s' %(device,name))
    print('完成拷贝日志')


