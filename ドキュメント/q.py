# coding: utf-8
import sys,codecs,os,time
qdic = {}
qlist = []
argvs = sys.argv
argc = len(argvs)
acount = 0
qcount = 0
mf = 0
if(argvs[2] == "Windows"):
    cle = "cls"
elif(argvs[2] == "Linux"):
    cle = "clear"

if(argvs[3] == "1"):
    mf = 1
def q():
    for key, value in di2.items():
        #clear
        os.system(cle)
        import __main__
        __main__.qcount += 1
        print(value)
        if(mf == 1):
            print("Show answer:",key)
        an = input("Your answer:")
        an.upper()
        f = codecs.open("incorrect.txt", "r", "utf-8")
        o = f.read()
        f.close()
        if (an == key):#正解した場合
            print("Correct")
            __main__.acount += 1
            print(value +" : "+ key)
        elif (an == "quit"):#quitを入力した場合
            __main__.qcount -= 1
            #__main__.acount -= 1
            p = round(float(__main__.acount) / __main__.qcount * 100)
            #変数pに回答率を代入
            print ("{0}門中、{1}門正解しました。正答率は{2}％です。".format(__main__.qcount, __main__.acount, p))
            quit()
        else:#不正解だった場合
            print(value +" : "+ key)
            if(key not in o):#間違えた問題の中に今回の問題が入っていなかった場合
                print("Incorrect")
                f = codecs.open("incorrect.txt", "a", "utf-8")
                istr = key+"|"+value+"\n"#この問題を間違えた問題集に追加
                f.write(istr)
                f.close()
                time.sleep(1)
            else:#そうでない場合
                print("Incorrect again")
                time.sleep(1)
                print(value +" : "+ key)
        print ("{0}門中、{1}門正解しています。".format(len(di2), acount))
        time.sleep(0.5)
if (argc != 4):#引数が2つでない場合
    print ("Usage: python3 %s filename os mode" % argvs[0])
    print ("mode:0=Nomal | 1=Show answer")
    quit()
    #print ("READ FILE >>> %s"% argvs[1])
f = codecs.open(argvs[1], "r", "utf-8")
line = f.readline()
while line:
    test = line.strip()
    list = test.split("|")#分割
    qlist = qlist + list#qlistにlistを追加
    line = f.readline()
    f.close
    di2 = dict(zip(qlist[0::2], qlist[1::2]))#qlistをディクショナリに(Key, vlau)
q()
p = round(acount / float(len(di2)) * 100)
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
        else:
            quit()
    else:
        quit()
else:
    quit()
