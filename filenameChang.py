import os
import re

def replaceDirName(rootDir)  
dirs = os.listdir(rootDir) 
for dir in dirs:   # 每一次循环都会执行一次，可以保证每次的结果换行
    print('oldname is:'+dir)   #注意是输出 dir ，不是dirs（文件夹下所有的文件包括子文件夹）。
    string = dir.split('.')
    num = string[0]  # 次级数组的第一项
     temp = "%03d"%int(num)+'_'+string[1]  #主要目的是再数字统一为3位，不够前面补0

    oldname = os.path.join(rootDir,dir)  #老文件夹的名字
    newname = os.path.join(rootDir,temp) #新文件夹的名字

    os.rename(oldname,newname)

if __name__=='_main_':
    rootDir = F:/下载/光盘/Java入门配套/daima'
    replaceDirName(rootdir)

# ##########
# ##########
#
# # Python读取文件夹下的所有文件
#
import os
path = "F:/" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
for file in files: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
          f = open(path+"/"+file); #打开文件
          iter_f = iter(f); #创建迭代器
          str = ""
          for line in iter_f: #遍历文件，一行行遍历，读取文本
              str = str + line
          s.append(str) #每个文件的文本存到list中
print(s) #

import os
path="F:/r_GFgd191/water"
files= os.listdir(path) # 获取所有文件夹下文件的名称，结果是数组
s=[]
for file in files:
    if not os.path.isdir(file)


# -*- coding: utf-8 -*-   
import time     
import os  
import shutil
 
 
def readFilename(path, allfile):
    filelist = os.listdir(path)
 
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath): #filepath 不是否是文件夹
            readFilename(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile
 
 
def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print "%s not exist!"%(srcfile)
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print "copy %s -> %s"%( srcfile,dstfile)
 
 
if __name__ == '__main__':
    
    path1="/Users/sunny/Desktop/123/"
    path2="/Users/sunny/Desktop/456/"
    path3="/Users/sunny/Desktop/789/"
    allfile1=[]
    allfile2=[]
	allfile1=readFilename(path1,allfile1)
    allfile2=readFilename(path2,allfile2)
    allname1=[]
    allname2=[]
    for name in allfile1:
        t=name.split("/")[-1][0:-4]
        print t
        allname1.append(t)
        print allname1
    for name in allfile2:
        t=name.split("/")[-1][0:-9]
        print t
        allname2.append(t)
        print allname2
    s1=[]
    for ff in allname1:
        f (ff not in allname2):
            s1.append(ff)
    print s1
    s2=[]
    for ff in allname1:
        if (ff in allname2):
            s2.append(ff)
    print s2
    for ns in s2:
        srcfile=path1+str(ns)+'.jpg'
        dstfile=path3+str(ns)+'.jpg'
        mycopyfile(srcfile,dstfile)


