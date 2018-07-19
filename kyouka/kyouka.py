# -*- coding:utf-8 -*-
kyouka = ["国語","社会","数学","理科","音楽","美術","保健体育","技術家庭","英語","その他"]
kyoukaa = ["国語","社会","数学","理科","音楽","美術","保健体育","技術家庭","英語","その他"]
kyouka1 = []
i = 0

def search_kyouka():
    for k1 in kyouka1:
        for k in kyouka:
           # print(k+":"+k1)
            if k in k1:
                if k in kyoukaa:
                    kyoukaa.remove(k)
                   # print("削除"+str(kyoukaa).decode("string-escape"))
    print(str(kyoukaa).decode("string-escape"))

print("一日目、二日目...最終日の順に教科予定を入力してください。(1入力ごとに一日)\n\r例(一日目):数学、理科、国語\n\rすべて入力できた場合はfinishと入力してください。")
while(1):
    i += 1
    nyuuryoku = raw_input()
    if(nyuuryoku == "finish"):
        break
    else:
        kyouka1.append(nyuuryoku)
search_kyouka()
