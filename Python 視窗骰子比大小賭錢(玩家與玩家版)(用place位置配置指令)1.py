import tkinter as s  #呼叫視窗套組，呼叫此套組的簡單名稱為s
import random as rand #呼叫亂數套組，呼叫此套組的簡單名稱為rand
def introductions() :
    w1=s.Tk()
    w1.title("介紹玩法")
    w1.geometry("270x270")
    lb1=s.Label(w1,text="雙方一開始先制定金額，代表接下來比大小")
    lb2=s.Label(w1,text="比一次輸贏的金額賭注。")
    lb3=s.Label(w1,text="然後誰先開始都可以，到最後玩家1跟玩家2")
    lb4=s.Label(w1,text="底下的Start按鈕各自都有點，才會算一次比")
    lb5=s.Label(w1,text="拚誰大誰小。")
    lb6=s.Label(w1,text="看要比幾次輸贏，由雙方玩家1跟玩家2事前")
    lb7=s.Label(w1,text="一起討論好在決定開始比拚。")
    lb1.place(x=10,y=10)
    lb2.place(x=10,y=35)
    lb3.place(x=10,y=70)
    lb4.place(x=10,y=95)
    lb5.place(x=10,y=120)
    lb6.place(x=10,y=145)
    lb7.place(x=10,y=170)
    w1.mainloop()
def clears() :
    global play1,play2,count1,count2,bouns1,bouns2
    eny1.delete(0,"end") #eny1清除entry，清到1個都不剩
    label11.configure(text="") #接下來label11開始由上至下到label44，各自都用configure指令
    label22.configure(text="") #然後放text=""，代表有清除的感覺
    label33.configure(text="")
    label44.configure(text="")
    play1=0 #玩家1金錢也歸0
    play2=0 #玩家2金錢也歸0
    count1=0 #玩家1比拚紀錄重新歸0
    count2=0 #玩家2比拚紀錄重新歸0
    bouns1=0 #玩家1骰子重新歸0
    bouns2=0 #玩家2骰子重新歸0
def s1() :
    global play1,play2,bouns1,bouns2,count1,count2
    count1=1 #一開始玩家1代表這一次骰骰子了，所以歸1，然後往下
    bouns1=rand.randint(1,6) #變數bouns為玩家1骰1~6骰子點數
    label11.configure(text=""+str(bouns1)) #這一次骰出來的點數轉str資料型態給label11呈現玩家1的骰子點數
    if count1==1 and count2==1 : #如果這一次比拚玩家1(count1)跟玩家2(count2)都骰了，那就進去
        if bouns1>bouns2 : #玩家1>玩家2，代表玩家1贏了
            money1=int(eny1.get()) #money1拿一開始設好的金額，轉int值給money1
            play1=play1+money1 #play1+money1，代表玩家1+錢
            label33.configure(text=""+str(play1)) #顯示玩家1目前的錢
        elif bouns1<bouns2 : #玩家1<玩家2，代表玩家2贏了
            money2=int(eny1.get()) #money2拿一開始設好的金額，轉int值給money2
            play2=play2+money2 #play2+money2，代表玩家2+錢
            label44.configure(text=""+str(play2)) #顯示玩家2目前的錢
        count1=0 #來到這邊代表中間過程已經OK了，所以歸0，為下一次重新一輪比拚
        count2=0 #來到這邊代表中間過程已經OK了，所以歸0，為下一次重新一輪比拚      
def s2() :
    global play1,play2,bouns1,bouns2,count1,count2
    count2=1 #一開始玩家2代表這一次骰骰子了，所以歸1，然後往下
    bouns2=rand.randint(1,6)
    label22.configure(text=""+str(bouns2))
    if count1==1 and count2==1 :
        if bouns1>bouns2 :
            money3=int(eny1.get())
            play1=play1+money3
            label33.configure(text=""+str(play1))
        elif bouns1<bouns2 :
            money4=int(eny1.get())
            play2=play2+money4
            label44.configure(text=""+str(play2))
        count1=0
        count2=0    

play1=0 #一開始先設一個play1,play1就是目前玩家1的獲得金錢的金額
play2=0 #一開始先設一個play2,play2就是目前玩家2的獲得金錢的金額
count1=0 #用來記玩家1有沒有這一次比拚已經骰過了，有骰為1沒骰為0
count2=0 #用來記玩家2有沒有這一次比拚已經骰過了，有骰為1沒骰為0
bouns1=0 #用來做為玩家1的骰子
bouns2=0 #用來做為玩家2的骰子
window=s.Tk()
window.title("玩家與玩家骰子比大小賭錢")
window.geometry("320x230+300+400")
window.resizable(1,0)
label1=s.Label(window,text="請選擇彼此下注金額: ",font=("Arial",10))
                             #font=("Arial",10)->font為控制文字字形及文字大小
                             #"Arial"就是文字字形 10就是文字大小
eny1=s.Entry(window,width=10)
lbintroduction=s.Button(window,text="介紹玩法",width=10,command=introductions) 
button1=s.Button(window,text="Clear",width=10,command=clears) #當按下此按鈕就觸發command=s2,s2函數名稱由下至上去尋找def遞迴函數
label2=s.Label(window,text="玩    家1: ")
label3=s.Label(window,text="玩    家2: ")
label11=s.Label(window,text="") #label11為待會控制玩家1的骰子點數
label0=s.Label(window,text="<-點數->",bg="#DC143C",width=8,height=1) #bg為文字欄位裡的背景顏色,width為背景顏色的寬度,寬度越大背景顏色就像一條線"橫的一樣"
                                                                     #height為背景顏色的長度,長度越大背景顏色就像一條線"直的一樣"
label22=s.Label(window,text="") #label22為待會控制玩家2的骰子點數
label33=s.Label(window,text="") #label33為待會控制玩家1的目前獲得金錢
label00=s.Label(window,text="<-賺$->",bg="#4169E1",width=7,height=1)
label44=s.Label(window,text="") #label44為待會控制玩家2的目前獲得金錢
button2=s.Button(window,text="Start",width=10,command=s1) #當按下此按鈕就觸發command=s1,s1函數名稱由下至上去尋找def遞迴函數
button3=s.Button(window,text="Start",width=10,command=s2)  
                                                                 
label1.place(x=10,y=0)
eny1.place(x=160,y=2)
lbintroduction.place(x=30,y=30)
button1.place(x=180,y=30)
label2.place(x=30,y=80)
label3.place(x=200,y=82)
label11.place(x=50,y=120)
label0.place(x=115,y=120)
label22.place(x=220,y=121)
label33.place(x=50,y=160)
label00.place(x=120,y=160)
label44.place(x=220,y=160)
button2.place(x=20,y=200)
button3.place(x=190,y=200)
window.mainloop()
