import os
import shutil
#清空目录

basefolder = '/Users/yetu/Downloads/multiscreenJar/'
def del_dir_tree(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)

exists  = os.path.exists(basefolder)
if exists:
    del_dir_tree(basefolder)  
else:
    os.makedirs(basefolder)

# 拷贝文件到merge
shutil.copy('/Users/yetu/work/qiyi/appstore/AppStoreDetailPage/libs/gson-2.2.4.jar', '/Users/yetu/Downloads/multiscreenJar/gson-2.2.4.jar')
shutil.copy('/Users/yetu/work/qiyi/tv8.4_bug_fixed/lib.framework/libs/multiscreen-r69144.jar', '/Users/yetu/Downloads/multiscreenJar/multiscreen-r69144.jar')

os.chdir('/Users/yetu/Downloads/multiscreenJar/')
jarlist = os.popen('ls').readlines() #这个返回值是一个list
print(jarlist)
for i in jarlist:
    comand = 'jar -xvf ' + i
    os.system(comand)
    print('释放', i)

os.system('rm -rf *.jar')
print('删除jar')

os.system('jar -cvfM multiscreen.jar .')

os.chdir("/Users/yetu/work/library/adt-bundle-mac-x86_64-20140702/sdk/build-tools/25.0.2/")

os.system('./dx --dex --output="/Users/yetu/work/qiyi/tv_devel/app.epg/src/main/assets/multiscreen-r69144.dex" "/Users/yetu/Downloads/multiscreenJar/multiscreen.jar"')
