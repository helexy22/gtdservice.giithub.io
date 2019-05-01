#-*- coding:utf-8 -*-

# 实现 GCP 数据的批量更新
# 更新数据直接覆盖原有 tif 文件
# 注意 arcpy.Warp_management 要求最低 arcgis 版本为10.2 

import arcpy
import os

gcppath = "D:\\181-0404\\181 - 副本\\181-GCP-ALL" #GCP 文件夹
stifpath = "D:\\181-0404\\181 - 副本\\181_2\\"    #待校正 tif 文件夹
mappath = "D:\\181-0404\\181 - 副本\\181_2\\tsxt\\" #校正后 tif 文件夹

gcppath = unicode(gcppath,'utf-8')
stifpath = unicode(stifpath,'utf-8') 
mappath = unicode(mappath,'utf-8') 

gcplist = os.listdir(gcppath)
filelist = os.listdir(stifpath)
for fs in filelist:
	fsextension = os.path.splitext(fs)[1]
	if fsextension == ".tif":
		fsname1 = os.path.splitext(fs)[0]
		fsname = fsname1[:26]
		for gcp in gcplist:
			gcpname1 = os.path.splitext(gcp)[1]
			gcpname = gcpname1[:26]
			if fsname == gcpname:
				gcptxt = gcpname1+".txt"
				stifname = fsname1+".tif"
				gcptifname = mappath+stifname
				arcpy.Warp_management(stifname,gcptifname,gcptxt,"POLYORDER1","",)
				print stifname+"success update"

				

