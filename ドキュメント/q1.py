# coding: utf-8
import sys,codecs,os,time
qdic = {}
qlist = []
argvs = sys.argv
argc = len(argvs)
acount=qcount=mf = 0
if (argc != 4):#引数が2つでない場合
    print ("Usage: python3 %s filename os mode" % argvs[0])
    print ("mode:0=Nomal | 1=Show answer")
    quit()
if(argvs[2] == "Windows"):
    cle = "cls"
elif(argvs[2] == "Linux"):
    cle = "clear"

def load():#問題文ロード関数
    f = codecs.open(argvs[1], "r", "utf-8")
    line = f.readline()
    while line:
        test = line.strip()
        list = test.split("|")#分割
        global qlist,di2
        qlist = qlist + list#qlistにlistを追加
        line = f.readline()
        f.close
        di2 = dict(zip(qlist[0::2], qlist[1::2]))#qlistをディクショナリに(Key, vlau)

def q():#クイズ関数
    import __main__
    for key, value in di2.items():
        f = codecs.open("incorrect.txt", "r", "utf-8")
        o = f.read()
        f.close()
        os.system(cle)
        __main__.qcount += 1
        print(value)#問題文表示
        if(argvs[3] == "1"):
            print("Show answer:",key)
        ans = input("Your answer:")
        ans.upper()
        if (ans == key):#正解した場合
            print("Correct")
            __main__.acount += 1
        elif (ans == "quit"):#quitを入力した場合
            __main__.qcount -= 1
            p = round(float(__main__.acount) / __main__.qcount * 100)
            print ("{0}門中、{1}門正解しました。正答率は{2}％です。".format(__main__.qcount, __main__.acount, p))
            quit()
        else:#間違えた場合
            if(key in o):#間違えた問題集の中に今回の問題が入っていた場合
                print("Incorrect again")
                #time.sleep(1)
            else:
                print("Incorrect")
                f = codecs.open("incorrect.txt", "a", "utf-8")
                istr = key+"|"+value+"\n"#この問題を間違えた問題集に追加
                f.write(istr)
                f.close()
        print(value +" : "+ key)
        print ("{0}門中、{1}門正解しています。".format(len(di2), acount))
        time.sleep(2)#二秒間待つ
load()#loadの実行
q()#qの実行
p = round(acount / float(len(di2)) * 100)#正答率の計算
print ("{0}門中、{1}門正解しました。正答率は{2}％です。".format(len(di2), acount, p))
if(p == 100):
    print("問題を全問正解することが出来ました。おめでとうございます。")
    if(argvs[1] == "incorrect.txt"):
        print("incorrect.txtの中身を消去しますか？Y/n")
        yn = input()
        if(yn == "Y"):
            f = codecs.open("incorrect.txt", "w", "utf-8")
            f.write("")
            f.close()
quit()
