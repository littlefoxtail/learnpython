import os
import shutil

import subprocess, signal
p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
out, err = p.communicate()
for line in out.splitlines():

    if './kcptun-darwin-amd64-20170525/client_darwin_amd64 -r 23.106.145.171:29900 -l :443 -mode fast3 -key very fast'.encode(encoding = 'utf-8') in line:
        pid = int(line.split(None, 1)[0])
        if 'sudo'.encode(encoding = 'utf-8') not in line:
            os.system('sudo kill -SIGINT %d' % (pid))
            print('已停止进程：', pid)

os.system("osascript -e 'quit app \"/Applications/ShadowsocksX-NG.app\"'")


