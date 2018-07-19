#-*- coding:utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime
import subprocess,codecs,sys,time,os
import gmail_v as gv
import google_search as gs
slist = []
idi2 = {}
ver = "Pre-Alpha_1.0.2"
username=""
userauthority=""
def jtalk(t):
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    #htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    htsvoice=['-m','/usr/share/hts-voice/rakan/戯歌ラカン.htsvoice']
    speed=['-r','1.0']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t)
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','open_jtalk.wav']
    wr = subprocess.Popen(aplay)

def say_text(text):
    jtalk(text.encode('utf-8'))
    print("Voynich:"+text)


def start_v():
    say_text("ヴォイニッチを起動します")
    load()
    time.sleep(1)
    os.system("clear")
    say_text("お呼びでしょうか、"+username+"さん。")

def load():
    global username
    global userauthority
    path_user = 'user_info.txt'
    print("user_info.txtの読み込み...")
    with open(path_user) as f:
        l = [s.strip() for s in f.readlines()]
        username = l[0]
        print("usernameの取得...done")
        userauthority = l[1]
        print("user_authorityの取得...done")

    f=codecs.open("word.txt","r","utf-8")
    line = f.readline()
    print("word.txtの読み込み...done")
    while line:
        test=line.strip()
        list = test.split("|")
        global slist,di2
        slist = slist+list
        line=f.readline()
        f.close
        di2 = dict(zip(slist[0::2], slist[1::2]))

def news():
    url = "http://news.yahoo.co.jp"
    with urlopen(url) as res:
        html = res.read().decode("utf-8")

        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('.ttl a')
        titles = [t.contents[0] for t in titles]
        [print(titles[i]) for i in range(8)]

def word():
    while(1):
        i_text = input()
        os.system("clear")
        if(i_text == "quit"):
            say_text("ヴォイニッチを終了します。")
            quit()
        elif(i_text in di2):
            k_value = di2[i_text]
            if("%username" in k_value):
                k_value = k_value.replace("%username",username)
            elif("%name" in k_value):
                k_value = k_value.replace("%name","ヴォイニッチ")
            elif("%time" in k_value):
                d = datetime.now()
                timetext = text = "%s月%s日、%s時%s分%s秒"%(d.month, d.day, d.hour, d.minute, d.second)
                k_value = k_value.replace("%time",timetext)
            else:
                k_value = di2[i_text]
            say_text(k_value)
        elif(i_text == "info"):
            text = "アシスタントシステムのヴォイニッチです。バージョンは以下の通りです。"
            say_text(text)
            print("version:"+ver)
        elif(i_text == "今日のニュース"):
            say_text("今日のニュースはこちらです。")
            news()
        elif(i_text == "メールを確認"):
            say_text("Gmailを確認します")
            gmail_text = gv.gmail_get_messages()
            print(gmail_text)
        elif("を検索して" in i_text or "とは" in i_text):
            if("を検索して" in i_text):
                i_text = i_text.replace("を検索して","")
            else:
                i_text = i_text.replace("とは","")
            gs.google_search(i_text)
            say_text(i_text+"を検索しました。")
start_v()
word()
