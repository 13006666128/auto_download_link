# -*- coding: utf-8 -*

import requests#网络请求
import re#提取数据
import time


URLadd1='%URL%'#分类URL头
URLadd2='%URL%'#子页面URL头

def auto_download_link_DEMO(pages):
  for n in range(1,pages):
   a_url='http://www.ygdy8.net/html/gndy/dyzz/list_23_'+str(n)+'.html'
   print('URL:',a_url)
   html_1=requests.get(a_url)
   html_1.encoding = 'gb2312'
   print('status code:',html_1.status_code) #200
   #print('网页源码：',html_1.text)  #查看网页源代码
   print('Process Page:',n)
   detil_list=re.findall('<a href="(.*?)" class="ulink',html_1.text)
   print('Deril list:',detil_list)
   for m in detil_list:
    #for m in detil_list[0]:提取一个
    b_url ='http://www.ygdy8.net/'+ m
    print('URL2:',b_url)
    html_2=requests.get(b_url)
    #指定网页编码格式
    html_2.encoding = 'gb2312'
    #print(html_2.text)
    #re.findall()返回列表
    ftp = re.findall('<a href="(.*?)">.*?</a></td>',html_2.text)
    print('FTP下载地址：',ftp)#打印查看
    with open('C:\\Users\\留学帮帮01\\Desktop\\dytt.txt','a',encoding='utf-8')as f:
    #写入本地 write写文本
     f.write(ftp[0]+'\n')

def auto_download_link(pages):
  index_1=0
  for n in range(1,pages):
   a_url=URLadd1+str(n)+'.html'
   print('分类 URL:',a_url)
   html_1=requests.get(a_url)
   html_1.encoding = 'utf-8'
   #print('status code:',html_1.status_code) #200
   #print('网页源码：',html_1.text)  #查看网页源代码
   print('处理第',n,'/',pages,'页面时间:',time.strftime('%Y-%m-%d %H:%M:%S'))
   detil_list=re.findall('<a href="(.*?)" style="color:',html_1.text)
   print('子页面数量:',len(detil_list))
   print('子页面清单:',detil_list)
   index_2=0
   for m in detil_list:
    #for m in detil_list[0]:提取一个
    b_url =URLadd2+ m
    index_1=index_1+1
    index_2=index_2+1
    print('开始处理新任务...')
    print('处理第',n,'/',pages,'主页面的',index_2,'/',len(detil_list),'子页面时间:',time.strftime('%Y-%m-%d %H:%M:%S'))
    print('子页面 URL:',b_url)
    html_2=requests.get(b_url)
    #指定网页编码格式
    html_2.encoding = 'utf-8'
    #print(html_2.text)
    #re.findall()返回列表
    ftp = re.findall(r"<ol><li>(.+)</ol>",html_2.text)
    if len(ftp) ==0:
     ftp='磁力链 is null'
    print('磁力链地址：',ftp)#打印查看
    with open('C:\\Users\\%username%\\Desktop\\磁力链.txt','a',encoding='utf-8')as f:
    #写入本地 write写文本
     f.write(ftp[0]+'\n')
     print('写文件时间:',time.strftime('%Y-%m-%d %H:%M:%S'),'累计写入次数：',index_1)
     print('任务成功')
     print('.')
     print('..')
     print('...')

xb_auto_download_link(211)
