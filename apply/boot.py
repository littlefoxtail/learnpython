import os
import time
return_code = os.popen('adb devices').readlines()
for line in return_code:
    if '192.168.3.12' not in line:
        noconnect = True
    else:
        noconnect = False
        break
if noconnect is True:
    os.system('adb connect 192.168.3.12')
    time.sleep(1)
os.system('adb shell am broadcast -a android.intent.action.BOOT_COMPLETED com.gala.video')
print('发送成功')