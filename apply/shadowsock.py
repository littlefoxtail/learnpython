import os
import shutil

os.chdir('/Users/yetu/work/shadowsocks/')
os.system('sh start_kc.sh')

os.system('open -a /Applications/ShadowsocksX.app')

print('开启成功')