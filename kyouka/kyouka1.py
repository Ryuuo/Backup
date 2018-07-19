# -*- coding:utf-8 -*-
kyouka = ['国語','社会','数学','理科','音楽','美術','保健体育','技術家庭','英語','その他']
kyoukaa = ["国語","社会","数学","理科","音楽","美術","保健体育","技術家庭","英語","その他"]
kyouka1 = []
def search_kyouka():
    ikyouka = ','.join(kyouka1) #リストを文字列に変換
    for k in kyouka: #kyoukaの要素数だけループ
        if k in ikyouka: #ikyoukaにkが入ってるなら
            kyoukaa.remove(k) #リストからkを削除
    print("\n\r今日の時点で持って帰る事が出来る教科は\n\r" + str(kyoukaa).decode("string-escape") + "\n\rです。")

print("一日目、二日目...最終日の順に教科予定を入力してください。(1入力ごとに一日)\n\r例:数学、理科、国語\n\r英語、音楽、美術\n\rすべて入力できた場合は finish と入力してください。")
print("教科名は以下の通りに入力してください。\n\r" + str(kyouka).decode("string-escape"))
while(1):
    nyuuryoku = raw_input() #入力
    if(nyuuryoku == "finish"): #finishが入力されたら
        break #ループから抜ける
    else:
        kyouka1.append(nyuuryoku) #入力した文字列をリストに追加
search_kyouka()
