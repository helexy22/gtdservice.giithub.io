import os
import re

def replaceDirName(rootDir)
dirs = os.listdir(rootDir)
for dir in dirs:
    print('oldname is:'+dir)   #输出老的名字

    string = dir.split('、')
    num = string[0]
    temp = "%03d"%int(num)+'_'+string[1]  #主要目的是再数字统一为3位，不够前面补0

    oldname = os.path.join(rootDir,dir)  #老文件夹的名字
    newname = os.path.join(rootDir,temp) #新文件夹的名字

    os.rename(oldname,newname)
if __name__=='_main_':
    rootDir = F:\下载\光盘\Java入门配套\daima'
    replaceDirName(rootdir)
