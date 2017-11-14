import os
import shutil
#清空目录


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

del_dir_tree('/Users/yetu/Downloads/mergejar/')  

# 拷贝文件到merge
shutil.copy('/Users/yetu/work/qiyi/appstore/AppStoreSDK/build/intermediates/bundles/debug/classes.jar', '/Users/yetu/Downloads/mergejar/classes.jar')
shutil.copy('/Users/yetu/work/qiyi/appstore/AppStoreDetailPage/build/intermediates/bundles/debug/classes.jar', '/Users/yetu/Downloads/mergejar/classes2.jar')
shutil.copy('/Users/yetu/work/qiyi/appstore/AppStoreDetailPage/libs/galaTask.jar', '/Users/yetu/Downloads/mergejar/galaTask.jar')
shutil.copy('/Users/yetu/work/qiyi/appstore/AppStoreDetailPage/libs/gson-2.2.4.jar', '/Users/yetu/Downloads/mergejar/gson.jar')
shutil.copy('/Users/yetu/work/qiyi/appstore/AppStoreDetailPage/libs/galaTask.jar', '/Users/yetu/Downloads/mergejar/galaTask.jar')
shutil.copy('/Users/yetu/work/qiyi/appstore/AppStoreDetailPage/libs/libAppManager_20170406.jar', '/Users/yetu/Downloads/mergejar/libAppManager_20170406.jar')
shutil.copy('/Users/yetu/work/qiyi/appstore/AppStoreDetailPage/libs/libDownloadManager_20170615.jar', '/Users/yetu/Downloads/mergejar/libDownloadManager_20170615.jar')
shutil.copy('/Users/yetu/work/qiyi/appstore/AppStoreDetailPage/libs/libTVGameUtils_20170406.jar', '/Users/yetu/Downloads/mergejar/libTVGameUtils_20170406.jar')
shutil.copy('/Users/yetu/work/qiyi/appstore/AppStoreDetailPage/libs/tvos_ui.jar', '/Users/yetu/Downloads/mergejar/tvos_ui.jar')

os.chdir('/Users/yetu/Downloads/mergejar/')
jarlist = os.popen('ls').readlines() #这个返回值是一个list
print(jarlist)
for i in jarlist:
    comand = 'jar -xvf ' + i
    os.system(comand)
    print('释放', i)

os.system('rm -rf *.jar')
print('删除jar')

os.system('jar -cvfM appstore.jar .')
