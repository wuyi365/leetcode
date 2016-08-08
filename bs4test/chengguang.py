#-- coding: gbk --

from bs4 import BeautifulSoup


from urllib import *
import urllib.request
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding=sys.stdout.encoding,errors='replace')

f = open('s.txt','rt', encoding='utf-8')

#print(f.read())

soup = BeautifulSoup(f.read(),"lxml")
z = soup.find_all('script')
for i in z:
    if 'gameTags' in i.get_text():
        print(i)
print('*****************************')
#x = soup.find('div',id='subscribe-alert-modal').find_next_siblings('script')
x = soup.find('div',id='subscribe-alert-modal').find_next('script')
print(len(x))
print(type(x))
print(x)
print('####################')
for i in x:
    print(type(i))
    print(len(i))
    #xx = i.previous_sibling()
    print(i)
    print('------')
    