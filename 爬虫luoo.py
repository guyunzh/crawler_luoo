# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os,re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
user_agent='Mozilla/4.0 (compatible;MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}

def music_page(page,headers):#通过给定页来获取页里所有期刊号信息
    r=requests.get('http://www.luoo.net/tag/?p='+str(page),headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    pattern=re.compile(r'(?<=vol\.)\d+')
    for mulu in soup.find_all(class_='meta rounded clearfix'):
        every_page_url = mulu.a.get('href')#每个期刊的url
        vol_number=re.search(pattern,str(mulu.a)).group()#每个期刊的刊号
        vol_name=mulu.a.get('title')#每个期刊的名字
        download_page(every_page_url,vol_name,vol_number,headers)

def download_page(every_page_url,vol_name,vol_number,headers=headers):#下载期刊音乐
    MusicUrl='http://mp3-cdn2.luoo.net/low/luoo/radio'
    r=requests.get(every_page_url,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    song_path=os.path.join(r"E:/ceshi",vol_name)#创建保存歌曲的文件夹，自己直接选定
    if not os.path.exists(song_path):#创建保存歌曲的文件夹
        os.mkdir(song_path)#创建保存歌曲的文件夹
        print '创建'+vol_name+'期刊'
        for url in soup.find_all(class_="track-item rounded"):
            song_name= url.find(class_="trackname btn-play").string#歌名
            song_mp3=MusicUrl+vol_number+'/'+song_name[:2]+'.mp3'#歌地址
            err=re.compile(r'[\|:<>/\\"\*\?]')
            song_name=re.sub(err,' ',song_name)
            with open(song_path+'/'+song_name[4:]+'.mp3','wb')as f:
                f.write(requests.get(song_mp3).content)
            print 'Download'+song_name+'----->finashed!'
    else :
        print 'There is exitdir!'
def vol_data(vol,headers=headers):#通过期刊号来获取信息
    volUrl='http://www.luoo.net/music/'+vol
    r=requests.get(volUrl,headers=headers)
    soup=BeautifulSoup(r.text,'html.parser')
    vol_name =soup.find(class_='vol-title').string# 期刊的名字
    download_page(volUrl, vol_name, vol, headers=headers)

if __name__=="__main__":
    want=raw_input("下载指定整页期刊输入y  \n下载指定期刊号输入n：")
    while True:
        if want=='y':
            page=raw_input("输入页码：")
            music_page(page, headers)
            break
        elif want=='n':
            vol=raw_input("输入三位期刊号：")
            vol_data(vol, headers)
            break
        else:
            print 'your input is error'
            want = raw_input("下载指定整页期刊输入y  \n下载指定期刊号输入n：")
