import tkinter as s
import random
def s1() : #由下至上s1函數名稱對該函數名稱,符合就進入
    global chstr,a1,a2,countw21,countw22,w3alls,w3a,w3b,arrnpc,arr,n,dataw4 #宣告函數,針對待會會用到的變數名稱
    global w1lb1,w1lb2,w1lb3,w1lb4,w1lb5,w2lb2,w2lb4,w2lb6,w2lb7,w3lb1,w3lb2,w3lb3,w3lb4,w3eny1,w4lb1
    chstr=eny1.get() #詳情請去python資料夾裡的->python視窗建立基礎指南->"Entry指令應用的筆記去看"
    if chstr=="1" :                    
        window1=s.Tk() #一開始的window1為tkinter裡的Tk()主視窗模組,所以window1先前不用下宣告函數global
        window1.title("剪刀石頭布")
        window1.geometry("230x200") #window1大小為230x200
        window1.resizable(0,0)
        w1lb1=s.Label(window1,text="玩家")
        w1lb2=s.Label(window1,text="") #w1lb2為玩家的出拳
        w1lb3=s.Label(window1,text="電腦")
        w1lb4=s.Label(window1,text="") #w1lb4為電腦的出拳
        w1lb5=s.Label(window1,text="") #w1lb5為比賽結果
        w1bt1=s.Button(window1,text="剪刀",width=5,command=w1s1) #當我按下此按鈕,就觸發該command=w1s1,w1s1函數名稱就會由下至上找def遞迴函數
                                                                #然後w1s1函數名稱對函數名稱
        w1bt2=s.Button(window1,text="石頭",width=5,command=w1s2) #當我按下此按鈕,就觸發該command=w1s2,w1s2函數名稱就會由下至上找def遞迴函數
                                                                #然後w1s2函數名稱對函數名稱
        w1bt3=s.Button(window1,text="布",width=5,command=w1s3) #當我按下此按鈕,就觸發該command=w1s3,w1s3函數名稱就會由下至上找def遞迴函數
                                                              #然後w1s3函數名稱對函數名稱
        w1btcl=s.Button(window1,text="Clear",width=5,command=w1s4) #當我按下此按鈕,就觸發該command=w1s4,w1s4函數名稱就會由下至上找def遞迴函數
                                                                   #然後w1s4函數名稱對函數名稱
        w1lb1.place(x=30,y=30)
        w1lb2.place(x=40,y=60)
        w1lb3.place(x=130,y=30)
        w1lb4.place(x=140,y=60)
        w1bt1.place(x=0,y=120)
        w1bt2.place(x=50,y=120)
        w1bt3.place(x=100,y=120)
        w1btcl.place(x=150,y=120)
        w1lb5.place(x=90,y=160)
        window1.mainloop()
    elif chstr=="2" :                               
        a1=0 #一開始先設a1為0,a1為玩家1骰子點數
        a2=0 #一開始先設a2為0,a2為玩家2骰子點數
        countw21=0 #countw21為玩家1贏的局數,一開始為0
        countw22=0 #countw22為玩家2贏的局數,一開始為0
        window2=s.Tk() #一開始window2為tkinter裡的Tk()主視窗模組,所以window1先前不用下宣告函數global
        window2.title("比大小")
        window2.geometry("210x170+130+100") #window2大小為210x170 130+100為執行時出現的螢幕位置
        window2.resizable(0,0)
        w2lb1=s.Label(window2,text="玩家1")
        w2lb2=s.Label(window2,text="") #w2lb2為待會玩家1骰子點數
        w2lb3=s.Label(window2,text="玩家2")
        w2lb4=s.Label(window2,text="") #w2lb4為待會玩家2的骰子點數
        w2lb0=s.Label(window2,text="贏局")
        w2lb6=s.Label(window2,text="") #w2lb6為玩家1贏的次數
        w2lb7=s.Label(window2,text="") #w2lb7為玩家2贏的次數
        w2bt1=s.Button(window2,text="Start1",width=5,command=w2s1) #當我按下此按鈕,就觸發該command=w2s1,w2s1函數名稱就會由下至上找def遞迴函數
                                                                  #然後w2s1函數名稱對函數名稱
        w2bt2=s.Button(window2,text="Start2",width=5,command=w2s2) #當我按下此按鈕,就觸發該command=w2s2,w2s2函數名稱就會由下至上找def遞迴函數
                                                                  #然後w2s2函數名稱對函數名稱                                                         
        w2bt3=s.Button(window2,text="Clear",width=5,command=w2s3) #當我按下此按鈕,就觸發該command=w2s3,w2s3函數名稱就會由下至上找def遞迴函數
                                                                 #然後w2s3函數名稱對函數名稱
        w2lb1.place(x=30,y=30)
        w2lb2.place(x=40,y=60)
        w2lb3.place(x=130,y=30)
        w2lb4.place(x=140,y=60)
        w2lb0.place(x=85,y=100)
        w2lb6.place(x=40,y=100)
        w2lb7.place(x=140,y=100)
        w2bt1.place(x=20,y=140)
        w2bt2.place(x=85,y=140)
        w2bt3.place(x=150,y=140)
        window2.mainloop()
    elif chstr=="3" :                
        w3alls=0 #一開始設一個c,c為0,c為總共在第幾次答對
        w3a=0 #一開始設一個a,a為0,a為幾a幾b中的a
        w3b=0 #一開始設一個b,b為0,b為幾a幾b中的b
        arrnpc=[] #一開始先設為空陣列,此陣列為電腦出題的陣列
        arr=[] #一開始先設空陣列,此陣列是他出題完用轉str資料型態後給他自己(電腦)
        window3=s.Tk() #一開始window3為tkinter裡的Tk()主視窗模組,所以window3先前不用下宣告函數global
        window3.title("幾A幾B")
        window3.geometry("250x160") #window3大小為250x160
        window3.resizable(0,0)
        w3eny1=s.Entry(window3,width=10)
        w3lb1=s.Label(window3,text="") #w3lb1為待會顯示幾A幾B中的幾A
        w3lb2=s.Label(window3,text="") #w3lb2為待會顯示幾A幾B中的幾B
        w3lb3=s.Label(window3,text="") #w3lb3為顯示答對後的電腦出題答案
        w3lb4=s.Label(window3,text="次數: ") #w3lb4為總共在第幾次答對
        w3bt1=s.Button(window3,text="遊戲說明",width=8,command=w3s1) #當我按下此按鈕,就觸發該command=w3s1,w3s1函數名稱就會由下至上找def遞迴函數
                                                                    #然後w3s1函數名稱對函數名稱
        w3bt2=s.Button(window3,text="電腦出題",width=8,command=w3s2) #當我按下此按鈕,就觸發該command=w3s2,w3s2函數名稱就會由下至上找def遞迴函數
                                                                    #然後w3s2函數名稱對函數名稱
        w3bt3=s.Button(window3,text="審查",width=8,command=w3s3) #當我按下此按鈕,就觸發該command=w3s3,w3s3函數名稱就會由下至上找def遞迴函數
                                                                #然後w3s3函數名稱對函數名稱
        w3bt4=s.Button(window3,text="Clear",width=8,command=w3s4) #當我按下此按鈕,就觸發該command=w3s4,w3s4函數名稱就會由下至上找def遞迴函數
                                                                 #然後w3s4函數名稱對函數名稱                                                        
        w3eny1.place(x=40,y=50)
        w3lb1.place(x=40,y=75)
        w3lb2.place(x=40,y=90)
        w3lb3.place(x=40,y=110)
        w3lb4.place(x=90,y=130)
        w3bt1.place(x=150,y=15)
        w3bt2.place(x=150,y=40)
        w3bt3.place(x=150,y=65)
        w3bt4.place(x=30,y=10)
        window3.mainloop()
    elif chstr=="4" :                
        n=0 #一開始設一個n,n為你前進目前的步數位置
        dataw4=["1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
        window4=s.Tk() #一開始window4為tkinter裡的Tk()主視窗模組,所以window4先前不用下宣告函數global
        window4.title("一維陣列直線賽跑")
        window4.geometry("550x150") #window4視窗大小480x150
        window4.resizable(0,0)
        w4lb0=s.Label(window4,text="起點->")
        w4lb1=s.Label(window4,text=str(dataw4)) #w4lb1是陣列跑步區域
                                               #text=str(dataw4)->把dataw4陣列丟入str括號裡當借值,然後轉str資料型態,之後該Label文字欄位為dataw4一維陣列
        w4lb2=s.Label(window4,text="<-終點")
        w4bt1=s.Button(window4,text="遊戲說明",width=8,command=w4s1) #當我按下此按鈕,就觸發該command=w4s1,w4s1函數名稱就會由下至上找def遞迴函數
                                                                    #然後w4s1函數名稱對函數名稱
        w4bt2=s.Button(window4,text="跑步",width=8,command=w4s2) #當我按下此按鈕,就觸發該command=w4s2,w4s2函數名稱就會由下至上找def遞迴函數
                                                                #然後w4s2函數名稱對函數名稱
        w4bt3=s.Button(window4,text="Clear",width=8,command=w4s3) #當我按下此按鈕,就觸發該command=w4s2,w4s2函數名稱就會由下至上找def遞迴函數
                                                                  #然後w4s2函數名稱對函數名稱                                                          
        w4lb0.place(x=5,y=50)
        w4lb1.place(x=50,y=50)
        w4lb2.place(x=440,y=50)                                    
        w4bt1.place(x=40,y=120)
        w4bt2.place(x=120,y=120)
        w4bt3.place(x=300,y=120)
        window4.mainloop()

def w1s1() : #由下至上w1s1函數名稱對該函數名稱,符合就進入
    global w1s11,w1npc1 #宣告函數,針對待會用到的變數名稱
    w1s11=1 #w1s11為自己的猜拳,1為剪刀
    w1npc1=random.randint(1,3) #w1npc1為亂數1-3隨機1個,代表出拳數
    if w1s11==1 : #w1s11是1就進去
        if w1npc1==1 : #進去後如果w1npc1是1就進去
            w1lb2.configure(text="剪刀") #玩家就為剪刀
            w1lb4.configure(text="剪刀") #電腦就為剪刀
            w1lb5.configure(text="平手!") #比賽結果為平手
        elif w1npc1==2 : #如果是2就進去
            w1lb2.configure(text="剪刀") #玩家就為剪刀
            w1lb4.configure(text="石頭") #電腦就為石頭
            w1lb5.configure(text="你輸了!") #比賽結果為你輸了
        elif w1npc1==3 : #如果是3就進去
            w1lb2.configure(text="剪刀") #玩家就為剪刀
            w1lb4.configure(text="布") #電腦就為布
            w1lb5.configure(text="你贏了!") #比賽結果為你贏了
def w1s2() : #由下至上w1s2函數名稱對該函數名稱,符合就進入
    global w1s22,w1npc2 #宣告函數,針對待會用到的變數名稱
    w1s22=2 #w1s22為自己的猜拳,2為石頭
    w1npc2=random.randint(1,3) #w1npc2為亂數1-3隨機1個,代表出拳數
    if w1s22==2 : #w1s22是2就進去
        if w1npc2==1 : #進去後如果w1npc2是1就進去
            w1lb2.configure(text="石頭") #玩家就為石頭
            w1lb4.configure(text="剪刀") #電腦就為剪刀
            w1lb5.configure(text="你贏了!") #比賽結果為你贏了
        elif w1npc2==2 : #如果是2就進去
            w1lb2.configure(text="石頭") #玩家就為石頭
            w1lb4.configure(text="石頭") #電腦就為石頭
            w1lb5.configure(text="平手!") #比賽結果為平手
        elif w1npc2==3 : #如果是3就進去
            w1lb2.configure(text="石頭") #玩家就為石頭
            w1lb4.configure(text="布") #電腦就為布
            w1lb5.configure(text="你輸了!") #比賽結果為你輸了
def w1s3() : #由下至上w1s3函數名稱對該函數名稱,符合就進入
    global w1s33,w1npc3  #宣告函數,針對待會用到的變數名稱
    w1s33=3 #w1s33為自己的猜拳,3為布
    w1npc3=random.randint(1,3) #w1npc3為亂數1-3隨機1個,代表出拳數
    if w1s33==3 : #w1s33是3就進去
        if w1npc3==1 : #進去後如果w1npc3是1就進去
            w1lb2.configure(text="布") #玩家就為布
            w1lb4.configure(text="剪刀") #電腦就為剪刀
            w1lb5.configure(text="你輸了!") #比賽結果為你輸了
        elif w1npc3==2 : #如果是2就進去
            w1lb2.configure(text="布") #玩家就為布
            w1lb4.configure(text="石頭") #電腦就為石頭
            w1lb5.configure(text="你贏了!") #比賽結果為你贏了
        elif w1npc3==3 : #如果是3就進去
            w1lb2.configure(text="布") #玩家就為布
            w1lb4.configure(text="布") #電腦就為布
            w1lb5.configure(text="平手!") #比賽結果為平手
def w1s4() : #由下至上w1s4函數名稱對該函數名稱,符合就進入
    w1lb2.configure(text="") #進入後先w1lb2做configure重新洗牌字串,變成括號裡的空字串
    w1lb4.configure(text="") #接下來的w1lb4跟w1lb5同樣w1lb2一樣動作
    w1lb5.configure(text="") #這樣做是類似於clear的作法

def w2s1() : #由下至上w2s1函數名稱對該函數名稱,符合就進入
    global a1 #宣告函數,針對等下會用到的變數名稱
    a1=random.randint(1,6) #a1為後方亂數1-6,1-6代表骰子1到6,看是亂數多少在給a1生成值
    w2lb2.configure(text=""+str(a1)) #w2lb2來到這邊configure重新洗牌字串,變成括號裡的字串
def w2s2() : #由下至上w2s2函數名稱對該函數名稱,符合就進入
    global a1,a2,countw21,countw22 #宣告函數,針對等下會用到的變數名稱
    a2=random.randint(1,6) #a2為後方亂數1-6,1-6代表骰子1到6,看是亂數多少在給a2生成值
    w2lb4.configure(text=""+str(a2)) #a2 OK之後,來到這邊,把w2lb4丟到這裡configure重新洗牌字串,變成括號裡的字串
    if a1>a2 : #接下來判斷勝負2種排列組合,先判斷a1點數大於a2的話,符合就進入
        countw21+=1 #a1大於的話,countw21獲得1勝+1
        w2lb6.configure(text=""+str(countw21)) #countw21 OK之後,來到這邊,把w2lb6丟到這裡configure重新洗牌字串,變成括號裡的字串
    elif a1<a2 : #如果a1點數小於a2的話,符合就進入
        countw22+=1 #a2比a1,a2獲勝,countw22獲得1勝+1
        w2lb7.configure(text=""+str(countw22)) #countw22 OK之後,來到這邊,把w2lb7丟到這裡configure重新洗牌字串,變成括號裡的字串
def w2s3() : #由下至上w2s3函數名稱對該函數名稱,符合就進入
    global a1,a2,countw21,countw22 #宣告函數,針對待會會用到的變數名稱           
    a1=0 #a1跟a2接連歸0
    a2=0
    countw21=0 #countw21跟countw22也接連歸0
    countw22=0
    w2lb2.configure(text="") #w2lb2到w2lb4 w2lb6 w2lb7陸續configure重新洗牌字串
    w2lb4.configure(text="") #變成括號裡的字串,由此可知此做法就像clear(清除)一樣
    w2lb6.configure(text="") #的道理
    w2lb7.configure(text="")

def w3s1() : #由下至上w3s1函數名稱對該函數名稱,符合就進入
    w3window1=s.Tk() #一開始w3window1為tkinter裡的Tk()主視窗模組,所以w3window1先前不用下宣告函數global
    w3window1.title("遊戲說明")
    w3window1.geometry("270x160+150+160")
    w3window1.resizable(0,0)
    w3w1lb1=s.Label(w3window1,text="1.一開始先按電腦出題按鈕,之後就是輸入你的")
    w3w1lb2=s.Label(w3window1,text=" 數字,然後再按審查按鈕,按到為4A為止就結")
    w3w1lb3=s.Label(w3window1,text=" 束了")
    w3w1lb4=s.Label(w3window1,text="2.Clear按鈕是可以清除的動作,可以清除後")
    w3w1lb5=s.Label(w3window1,text=" 再來一局!")
    w3w1lb1.place(x=10,y=10)
    w3w1lb2.place(x=15,y=30)
    w3w1lb3.place(x=15,y=50)
    w3w1lb4.place(x=10,y=80)
    w3w1lb5.place(x=15,y=100)
    w3window1.mainloop()
def w3s2() : #由下至上w3s2函數名稱對該函數名稱,符合就進入
    global arrnpc,arr #宣告函數,針對待會會用到的變數名稱
    arrnpc=[] #先確保一次,arrnpc陣列先變空陣列
    arr=[] #先確保一次,arr陣列先變空陣列
    for i in range(0,1,1) : #此for i是先取第一個值
        arrnpc+=[random.randint(1,9)] #第一個值限定1-9
    for j in range(1,4,1) : #此for j是取剩下2-4的值,0-9範圍
        arrnpc+=[random.randint(0,9)]
        for k in range(0,j,1) :
            if arrnpc[k]==arrnpc[j] :
                arrnpc[j]=random.randint(0,9)
                if arrnpc[k]==arrnpc[j] :
                    arrnpc[j]=random.randint(0,9)
    for x in range(0,4,1) :
        arr+=[str(arrnpc[x])]
def w3s3() :
    global w3a,w3b,w3alls,data,users #宣告函數,針對待會會用到的變數名稱
    w3a=0 #w3a先確保先在這裡歸0
    w3b=0 #w3b先確保先在這裡歸0
    data=[] #data在這裡設一個空陣列
    users=w3eny1.get() #users在這裡為後方w3eny1空白欄位上的字串值,用get()函數去給他自己(users)做生成值
    for i1 in range(0,4,1) : #for i1為分割users字串,分割成單字串丟給data一維陣列
        data+=[users[i1]] #每循環1次data就+ users的i1位置值的單字串
    for i2 in range(0,4,1) : #這裡是審查迴圈
        if i2==0 : #如果i2是0的話就進入
            if data[i2]==arr[i2] : #如果雙方0位置值的單字串是一樣,代表1個吻合正確,w3a就+1
                w3a+=1
            elif data[i2]==arr[1] or data[i2]==arr[2] or data[i2]==arr[3] : #如果0沒有的話,就看值1 值2 值3有沒有一樣,一樣就進去
                w3b+=1 #進去代表b,所以w3b就+1
        elif i2==1 : #意思與上方 if i2==0 : 一樣意思
            if data[i2]==arr[i2] :
                w3a+=1
            elif data[i2]==arr[0] or data[i2]==arr[2] or data[i2]==arr[3] :
                w3b+=1
        elif i2==2 :
            if data[i2]==arr[i2] :
                w3a+=1
            elif data[i2]==arr[0] or data[i2]==arr[1] or data[i2]==arr[3] :
                w3b+=1
        elif i2==3 :
            if data[i2]==arr[i2] :
                w3a+=1
            elif data[i2]==arr[0] or data[i2]==arr[1] or data[i2]==arr[2] :
                w3b+=1
    w3lb1.configure(text=""+str(w3a)+" A") #每次審查完畢後,看目前幾a幾b
    w3lb2.configure(text=""+str(w3b)+" B")
    w3alls+=1 #次數也丟進來這邊做+1的動作
    w3lb4.configure(text="次數: "+str(w3alls)) #w3lb4來到這邊configure重新洗牌字串,變成括號裡的字串
    if w3a==4 : #如果w3a==4,代表w3a是4A,那就進去
        w3lb3.configure(text="電腦出題為: "+str(arr)) #顯示電腦出題!代表核對答案和結束意思
def w3s4() : #由下至上w3s4函數名稱對該函數名稱,符合就進入
    global w3alls,w3a,w3b,arrnpc,arr #宣告函數,針對待會會用到的變數名稱
    w3alls=0 #w3alls歸0 w3a歸0 w3b歸0
    w3a=0
    w3b=0
    arrnpc=[] #arrnpc陣列歸空陣列 arr陣列歸空陣列
    arr=[]
    w3lb1.configure(text="") #w3lb1丟到這邊做configure重新洗牌字串,變成括號裡的空字串
    w3lb2.configure(text="") #w3lb2 w3lb3 w3lb4依序一模一樣動作,這樣做有類似於clear(清除)
    w3lb3.configure(text="") #動作
    w3lb4.configure(text="")
    w3eny1.delete(0,"end") #把w3eny1(Entry)空白欄位丟來這邊做刪除動作,然後"end",就是針對該空白欄位做字串清除
                          #,接下來的0就是有幾個字串就清幾個,清到一個都不剩

def w4s1() : #由下至上w4s1函數名稱對該函數名稱,符合就進入
    w4window1=s.Tk() #一開始w4window1為tkinter裡的Tk()主視窗模組,所以w4window1先前不用下宣告函數global
    w4window1.title("遊戲說明")
    w4window1.geometry("250x150+130+200")
    w4window1.resizable(0,0)
    w4w1lb1=s.Label(w4window1,text="1.建議遊戲兩人較剛好")
    w4w1lb2=s.Label(w4window1,text="2.兩個人看誰先誰後,之後先的人執行一次")
    w4w1lb3=s.Label(w4window1,text=",後的人再跟著執行一次,以此類推看誰到")
    w4w1lb4=s.Label(w4window1,text="達最後一個,就為獲勝!")
    w4w1lb5=s.Label(w4window1,text="3.要在下一局比賽就按Clear清除按鈕即可")
    w4w1lb1.place(x=10,y=10)
    w4w1lb2.place(x=10,y=35)
    w4w1lb3.place(x=15,y=60)
    w4w1lb4.place(x=15,y=85)
    w4w1lb5.place(x=10,y=110)
    w4window1.mainloop()
def w4s2() : #由下至上w4s2函數名稱對該函數名稱,符合就進入
    global k1,summk,j1,n,dataw4 #宣告函數,針對待會會用到的變數名稱
    k1=n #k1先拿n的值,待會要看目前位置在哪
    summk=0 #一開始summk先歸0,待會要由他亂數產生跑步步數
    if k1==14 or k1==15 or k1==16 or k1==17 or k1==18 : #如果檢查步數,目前是14-18則進入
        if k1==14 : #k1是14則進入
            summk=random.randint(0,5) #代表離終點19,只剩5步,所以亂數產生0-5就好
        elif k1==15 : #k1是15則進入
            summk=random.randint(0,4) #代表離終點19,只剩4步,所以亂數產生0-4就好
        elif k1==16 : #k1是16則進入
            summk=random.randint(0,3) #代表離終點19,只剩3步,所以亂數產生0-3就好
        elif k1==17 : #k1是17則進入
            summk=random.randint(0,2) #代表離終點19,只剩2步,所以亂數產生0-2就好
        elif k1==18 : #k1是18則進入
            summk=random.randint(0,1) #代表離終點19,只剩1步,所以亂數產生0-1就好
    else : #如果不是14-18則來到else這
        summk=random.randint(0,6) #進入後來到這,就正常亂數0-6
    j1=n #來到這邊,代表我由上至下生成下一步數了,所以接下來要把目前步數所在地歸0
    if j1==0 :
        dataw4[0]="0"
        w4lb1.configure(text=""+str(dataw4)) #str(dataw4)->把目前最新值dataw4陣列丟到這當借值,轉str資料型態
    elif j1==1 :
        dataw4[1]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==2 :
        dataw4[2]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==3 :
        dataw4[3]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==4 :
        dataw4[4]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==5 :
        dataw4[5]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==6 :
        dataw4[6]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==7 :
        dataw4[7]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==8 :
        dataw4[8]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==9 :
        dataw4[9]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==10 :
        dataw4[10]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==11 :
        dataw4[11]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==12 :
        dataw4[12]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==13 :
        dataw4[13]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==14 :
        dataw4[14]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==15 :
        dataw4[15]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==16 :
        dataw4[16]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==17 :
        dataw4[17]="0"
        w4lb1.configure(text=""+str(dataw4))
    elif j1==18 :
        dataw4[18]="0"
        w4lb1.configure(text=""+str(dataw4))
    n+=summk #接下來就是目前步數+下一步
    if n>=0 and n<=18 : #如果n是0到18步就進入
        if n==0 :
            dataw4[0]="1"
            w4lb1.configure(text=""+str(dataw4)) #str(dataw4)->把目前最新值dataw4陣列丟到這當借值,轉str資料型態
        elif n==1 :
            dataw4[1]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==2 :
            dataw4[2]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==3 :
            dataw4[3]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==4 :
            dataw4[4]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==5 :
            dataw4[5]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==6 :
            dataw4[6]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==7 :
            dataw4[7]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==8 :
            dataw4[8]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==9 :
            dataw4[9]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==10 :
            dataw4[10]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==11 :
            dataw4[11]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==12 :
            dataw4[12]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==13 :
            dataw4[13]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==14 :
            dataw4[14]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==15 :
            dataw4[15]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==16 :
            dataw4[16]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==17 :
            dataw4[17]="1"
            w4lb1.configure(text=""+str(dataw4))
        elif n==18 :
            dataw4[18]="1"
            w4lb1.configure(text=""+str(dataw4))
    elif n==19 :
        dataw4[19]="1"
        w4lb1.configure(text=""+str(dataw4)) #str(dataw4)->把目前最新值dataw4陣列丟到這當借值,轉str資料型態
def w4s3() : #由下至上w4s3函數名稱對該函數名稱,符合就進入
    global n,dataw4 #宣告函數,針對待會會用到的變數名稱
    n=0 #n就歸0
    dataw4=["1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"] #dataw4一維陣列就歸原本那樣
    w4lb1.configure(text=""+str(dataw4)) #w4lb1文字欄位也來到這邊,然後configure重新洗牌字串,變成括號裡的字串
                                        #這樣的做法也有如Clear(清除)作用
    
window=s.Tk()
window.title("小遊戲樂園")
window.geometry("295x220+120+130")
window.resizable(0,0)
lb0=s.Label(window,text="輸入 ",font=("標楷體",12)) #font為控制文字欄位的文字字形與文字大小
eny1=s.Entry(window,width=10)
lb1=s.Label(window,text="號碼查詢",font=("新細明體",10)) #font為控制文字欄位的文字字形與文字大小
lb2=s.Label(window,text="1.剪刀石頭布",font=("新細明體",10)) #font為控制文字欄位的文字字形與文字大小
lb3=s.Label(window,text="2.比大小",font=("新細明體",10)) #font為控制文字欄位的文字字形與文字大小
lb4=s.Label(window,text="3.幾A幾B",font=("新細明體",10)) #font為控制文字欄位的文字字形與文字大小
lb5=s.Label(window,text="4.一維陣列直線賽跑",font=("新細明體",10)) #font為控制文字欄位的文字字形與文字大小
bt1=s.Button(window,text="Start",width=7,command=s1) #當我按下此按鈕,就觸發該command=s1,s1函數名稱就會由下至上找
                                                     #def遞迴函數,然後s1函數名稱對函數名稱
lb0.place(x=55,y=45)
eny1.place(x=40,y=80)
lb1.place(x=160,y=30)
lb2.place(x=165,y=55)
lb3.place(x=165,y=80)
lb4.place(x=165,y=105)
lb5.place(x=165,y=130)
bt1.place(x=50,y=120)
window.mainloop()
#
