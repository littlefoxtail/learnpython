# -*- coding:utf-8 -*-

import os
import re
import subprocess


def get_devices(adb_path='adb'):
    with open(os.devnull, 'wb') as devnull:
        subprocess.check_call([adb_path, 'start-server'], stdout=devnull,
                              stderr=devnull)
    out = split_lines(
        subprocess.check_output([adb_path, 'devices']).decode('utf-8'))
    # The first line of `adb devices` just says "List of attached devices", so
    # skip that.
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
    # rstrip is used here to workaround a difference between splineslines and
    # re.split:
    # >>> 'foo\n'.splitlines()
    # ['foo']
    # >>> re.split(r'\n', 'foo\n')
    # ['foo', '']
    return re.split(r'[\r\n]+', s.rstrip())
devices = get_devices()

print("有这么几个设备",devices)


for device in devices:
    print("设备：", device)
    # model = os.popen('adb -s %s shell getprop ro.product.model' %(device)).readlines()
    model = subprocess.check_output(['adb','-s', device, 'shell', 'getprop', 'ro.product.model']).decode('utf-8')
    print("展小燕的model:", model)
    print("开始Push：")
    os.system('adb -s %s push monkey.jar /sdcard' %(device))
    os.system('adb -s %s push framework.jar /sdcard' %(device))
    os.system('adb -s %s push max.xpath.actions /sdcard' %(device))
    os.system('adb -s %s push max.xpath.selector /sdcard' %(device))
    os.system('adb -s %s push max.widget.black /sdcard' %(device))
    os.system('adb -s %s push max.config /sdcard' %(device))
    os.system('adb -s %s push leak_upload.config /sdcard' %(device))
    print("完成Push:")

    print('开始执行monkey')
    os.system('adb -s %s shell CLASSPATH=/sdcard/monkey.jar:/sdcard/framework.jar exec app_process /system/bin tv.panda.test.monkey.Monkey -p com.sina.weibo --uiautomatormix --running-minutes 100 -v -v' %(device))
    print('完成执行monkey')



