#coding:utf-8
import urllib
import os
import sys
url4=['']*20
url3=['']*20
url5=['']*20
shu=int(raw_input("input where to begin(big number,three digit):"))
shu2=int(raw_input("input where to stop(small number,three digit):"))
if shu<=000 or shu2<=000:
   print 'your input is error'
   sys.exit(0)
kkk=int(raw_input('please input from which one to download the song,press "Enter" to end:'))
if kkk<=0:
   print 'your input is error'
   sys.exit(0)
else :
   kkk=kkk-1
if shu<shu2:
   print 'your input is error'
   sys.exit(0)
print 'finish means the music is downloaded.if you want to stop ,press "Ctrl+C" '
sss=1
dizhi=raw_input("where do you want to save(such as ' F:/.../ 'you'd better not choise chinese):")
print '----------------------------------------------------------------------------'
print '----------------------------------------------------------------------------'
while shu>=shu2:
   print 'start downloading vol.',shu
   url=('http://www.luoo.net/music/'+str(shu))
   con=urllib.urlopen('http://www.luoo.net/music/'+str(shu)).read()
   track=con.find(r'track_')
   m=0
   while track!=-1:
      one=con[track+6:track+11]
      two=con.find(r'track-name',track)
      url5[m]=one
      track=con.find(r'track_',two)
      m=m+1
   i=0
   if not os.path.exists(str(dizhi)+'vol.'+str(shu)):
         os.makedirs(str(dizhi)+'vol.'+str(shu))
   j=kkk
   while j<m:
      url2='http://www.luoo.net/single/'+ url5[j]
      content=urllib.urlopen('http://www.luoo.net/single/'+url5[j]).read()
      track=content.find(r'track-name')
      p=content.find(r'</p>',track)
      url3[i]=content[track+12:p].decode('utf-8')
      mp3=content.find(r'.mp3')
      http=content.find(r'http',mp3-100)
      url4[i]=content[http:mp3+4]
      url4[i]=url4[i].replace('\\','')
      print '   sum=',sss,'...downloading>>>>',url3[i]
      music=urllib.urlopen(url4[i]).read()   
      try:
         open(str(dizhi)+'vol.'+str(shu)+'/'+url3[i].encode('GBK')+'.mp3','wb').write(music)
      except:
         open(str(dizhi)+'vol.'+str(shu)+'/'+str(i+1)+'.mp3','wb').write(music)   
      i=i+1
      j=j+1
      sss=sss+1
      print '       finish!'
   print 'vol.',shu,'is finished!'
   shu=shu-1
print 'All Over'
print '                          >>>>>>>>>>>>>>>>>>>>>'
print '                          >>made by Zhao Hang>>'
print '                          >>>>>>>>>>>>>>>>>>>>>'
print 'press "Ctrl + C" or "Enter" to exit'
end=raw_input()


