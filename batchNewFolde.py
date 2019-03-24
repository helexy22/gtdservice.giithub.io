# # print("成功解决中文编码的问题")
# # print "'你好'"
# import pci
# # print ("nihao")
# print "ni"

import os, sys
def genDir():
    base = 'E:\\QQDownload\\Master111\\0323野外照片\\'
    i = 1
    for j in range(19):
        file_name = base + "#"+str(i)  #此处使用int(i)会出错
        os.mkdir(file_name)
        i=i+1
genDir()
print("批量新建文件夹成功")

