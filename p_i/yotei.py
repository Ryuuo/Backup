#-*- coding:utf8 -*-
import sys
c = []
s = []
res = []

argvs = sys.argv
argc = len(argvs)
if(argc != 3):
    print("引数が足りません。\n\r使い方:python %s 時間割表のファイル名[table.txt] 予定表のファイル名[schedule.txt]"% argvs[0])
    quit()

def Put(str,str1):
    if(str == "reading"):
        print("Reading<%s>...done"%(str1))
    elif(str == "error"):
        print(u"[Error]%sの読み込みでエラーが発生しました。")

def Reading_a_text_file():#テキストファイルの読み込み
#table.txt
    try:
        txt_data = open(argvs[1],"r")
    except:
        Put("error","table.txt")
    for txt_data_line in txt_data:
        line = txt_data_line.rstrip('\r\n')
        c.append(line)
    txt_data.close()
    Put("reading","table.txt")
#schedule.txt
    try:
        Schedule_data = open(argvs[2],"r")
    except:
        Put("error","schedule.txt")
    for schedule_data_line in Schedule_data:
        schedule_data_line.strip("\r\n")
        s.append(schedule_data_line)
    Schedule_data.close()
    Put("reading","schedule.txt")

def Conversion():#変換処理
    for d_line in s:
        res = []
        Split_line = d_line.split("/")
        for split_d_line in Split_line:
            i = int(split_d_line) - 1
            res.append(str(c[i]))
        print(str(res).decode("string-escape"))

Reading_a_text_file()
Conversion()
