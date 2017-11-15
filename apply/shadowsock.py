import os
import shutil

os.system('open -a /Applications/ShadowsocksX.app')
os.chdir('/Users/yetu/work/shadowsocks/')
os.system('echo "521484"|sudo -S ./kcptun-darwin-amd64-20170525/client_darwin_amd64 -r "23.106.145.171:29900" -l ":443" -mode fast3 -key "very fast"')
print('开启成功')