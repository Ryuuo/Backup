def vendingmachine(money):
    if(money > 100):
        if(money == 160):
            print("アクエリアスを買うことができました。")
        elif(money > 160):
            change = money - 160
            print("%s円のお釣りです。"%(change))
        elif(money < 160):
            print("現時点で、160円以下の商品は入荷しておりません。")
    elif(money < 100):
        print("100円以下なので何も買うことができません。")
    else:
        print("お金ではない可能性があります。(半角の数字で入力してください)")

while(1):
    money1 = input()
    vendingmachine(money1)
