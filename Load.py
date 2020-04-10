import requests
import re
import os

def getHTML(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding="utf-8"
        return r.text
    except:
        print( '1')

def getpiclist(text):
    try:
        ls=re.findall(r'https://imgsa.baidu.com/forum/w%3D580/sign=[a-z0-9]+/[a-z0-9]+.jpg',text)
        return ls
    except:
        print( '2')

def getpic(lists,n):
    try:
        count=0
        for url in lists[:n]:
            
            root="F://pics//"
            path=root+url.split('/')[-1]
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):   
                r=requests.get(url)
                r.raise_for_status()
                with open(path,'wb') as f:
                    f.write(r.content)
                    f.close()
            count=count+1
            pragrass(count,n)
            
    except:
        print('3')
def pragrass(i,n):
    per=int(round(i/n,2)*50)
    a='*'*per
    b='.'*(50-per)
    print('\r已下载{}张[{}->{}]'.format(i,a,b),end='')



def main():
    textlist=[]
    textlistall=[]
    number=eval(input("请输入需要下载图片的数量:"))
    m=1
    while len(textlistall)<=number:
        url="https://tieba.baidu.com/p/3548625993?pn="+chr(m)
        text = getHTML(url)
        textlist=getpiclist(text)
        textlistall=textlistall+textlist
        m=m+1
       
    print("开始下载")
    getpic(textlistall,number)
    print("下载完成")
main()
