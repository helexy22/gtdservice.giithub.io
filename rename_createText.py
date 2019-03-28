## 读取目录中的.txt文件
## 功能重命名文件，新建txt,并且写入txt

import os
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

src_dir_path = 'F:/r_GFgd191/water/change/'   # 文件夹后面的/是必须的，因为/可以区分文件和文件夹  #输入文件的位置
toSrc_dir_path = 'F:/r_GFgd191/water/change/new/'                                             #输出文件的位置

### 判断输出文件夹是否存在，如果不存在就新建文件夹
newfolder=os.path.exists(toSrc_dir_path)    
if not newfolder:
        os.makedirs(toSrc_dir_path)    # os.makedirs新建文件夹
        print("creater !toSrc_dir_path!  success ")
else:
	print ('---  There is this folder!  ---')

key = '.tif'                           #需要重命名文件的后缀
newfiletype=".txt"                     #新增加文件的后缀

dirs=os.listdir(src_dir_path)
for dir in dirs:
    if key in dir:   #只读取含key的文件
        string1 = dir.split('.tif')
        string2 = dir.split('_')
        filename="GF1_"+string1[0]

        ### tif文件重命名
        temp=filename+".tif"    #新文件名必须带后缀
        oldname = os.path.join(src_dir_path,dir) 
        newname = os.path.join(src_dir_path,temp)
        os.rename(oldname,newname)
        print("rename success")

        ### 判断水质参数的名称
        watercalss=string2[4].split('.')
        string2[4]=watercalss[0]
        if string2[4]=='u':   #1
                imagecalss="COD浓度图像"
        elif string2[4]=='ucol':
                imagecalss="COD浓度专题图"  
        elif string2[4]=='al':
                imagecalss="水华指数图像"  #2
        elif string2[4]=='alcol':
                imagecalss="水华指数专题图"
        elif string2[4]=='s':
                imagecalss="混浊度图像" #3
        elif string2[4]=='scol':
                imagecalss="混浊度专题图"  
        elif string2[4]=='c':
                imagecalss="叶绿素浓度图像" #4 
        elif string2[4]=='ccol':
                imagecalss="叶绿素浓度专题图"
        elif string2[4]=='cls':   #5
                imagecalss="水质综合等级图像"
        elif string2[4]=='clscol':
                imagecalss="水质综合等级专题图"
        else:
                imagecalss="其他"
                print(string2[4]+"-----的文件名错误------！！！！！！，文件编号:"+string1[0])
        # 优化方向将if语句转为一个数组，数组中的元素一一对应

        ### 在设定目录下新建txt文件，并写入msg
        msg="卫星：GF-1"'\n'+'传感器类型：'+string2[0] +'\n'+"成像时间："+string2[3]+'\n'+"产品类型："+ imagecalss+'\n'+"生产单位：中山大学"   #txt文件中输入的内容
        ol=open(toSrc_dir_path+filename+newfiletype,'w')  
        ol.write(msg)
      
print('运行成功')
