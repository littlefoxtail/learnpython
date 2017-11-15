import os
import shutil

os.system('open -a /Applications/ShadowsocksX.app')
os.chdir('/Users/yetu/work/shadowsocks/')
os.system('sh start_kc.sh')

print('开启成功')