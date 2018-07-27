import os
import subprocess

model = subprocess.check_output(['adb','shell', 'getprop', 'ro.product.model']).decode('utf-8')
print(model)
current_path = os.path.abspath(os.path.dirname(__file__))
folder = '%s/test_result/%s' %(current_path, model)
print(folder)
exists  = os.path.exists(folder)



if not exists:
    os.makedirs(folder)