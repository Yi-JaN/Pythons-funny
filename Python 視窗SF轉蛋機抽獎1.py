import tkinter as s
import random
def s1() : #s1函數名稱對該def s1() :函數名稱,符合就進入
    global bingo,me #針對待會會用到的變數名稱做global宣告函式
    if me>0 : #然後由上至下run,一開始是先審查if me>0 ,符合就進去該if裡面
        me=me-1 #me就先-1,代表已經抽一顆轉蛋掉
        if me==bingo : #接下來me跟bingo的值如果是一樣就進入,代表中大獎
            s.messagebox.showinfo(title="中獎!",message="恭喜獲得X-MAS PSG-1") #呼叫tkinter模組裡的messagebox彈跳視窗的模組包,
                                                                             #從該模組包裡呼叫showinfo彈跳視窗,針對該showinfo設title(標題)
                                                                             #跟message(內容物)
            me=250 #me重新歸250,意思是做下一次的轉蛋,這次轉蛋已結束
            bingo=random.randint(0,249) #bingo跟一開始先設中獎號碼一樣,0-249重新定一個新的中獎號碼,代表做下一次的轉蛋大獎號碼,這次轉蛋已結束
            lb0.configure(text="Cash "+str(me)+"/250") #configure為重新洗牌該lb0文字模組裡的文字字串,然後再變成括號字串
        else : #如果沒有一樣就往下來到這邊,else無條件進入,所以就進去
            lb0.configure(text="Cash "+str(me)+"/250") #configure為重新洗牌該lb0文字模組裡的文字字串,然後再變成括號字串
            n=random.randint(1,12) #n為貳獎及其餘獎項,因為會進來這裡代表沒中大獎
            if n==1 :
                s.messagebox.showinfo(title="中獎!",message="獲得X-MAS PSG-1 1天")
            elif n==2 :
                s.messagebox.showinfo(title="中獎!",message="獲得貳獎PSG-1 3天")
            elif n==3 :
                s.messagebox.showinfo(title="中獎!",message="獲得貳獎PSG-1 1天")
            elif n==4 :
                s.messagebox.showinfo(title="中獎!",message="獲得點數SP增加 1天")
            elif n==5 :
                s.messagebox.showinfo(title="中獎!",message="獲得經驗值加倍 3天")
            elif n==6 :
                s.messagebox.showinfo(title="中獎!",message="獲得武器增加C,D 3天")
            elif n==7 :
                s.messagebox.showinfo(title="中獎!",message="獲得貳獎PSG-1 3天")
            elif n==8 :
                s.messagebox.showinfo(title="中獎!",message="獲得經驗值加倍 1天")
            elif n==9 :
                s.messagebox.showinfo(title="中獎!",message="獲得隨機人物1個1天")
            elif n==10 :
                s.messagebox.showinfo(title="中獎!",message="獲得武器增加C,D 1天")
            elif n==11 :
                s.messagebox.showinfo(title="中獎!",message="獲得點數SP增加 3天")
            elif n==12 :
                s.messagebox.showinfo(title="中獎!",message="獲得隨機人物1個1天")

bingo=random.randint(0,249) #一開始先設bingo,bingo為中獎號碼,因為從250開始點會扣1,所以就是中獎號碼為0-249之間,
                            #那0+249剛好就為250個轉蛋
me=250 #me為轉蛋數量,一開始設個me為250,之後每點1下扣1                            
window=s.Tk()
window.title("SF超級轉蛋機")
window.geometry("420x380+400+250")
window.resizable(0,0) #(0,0)為前面的0是針對寬度(width)設0,後0是針對長度(height)設0
                      #這樣子做是因為針對window視窗做無法放大視窗只能用當前視窗大小使用方式
window.configure(bg="grey") #這裡所用的configure是針對window變數名稱的視窗,而由上至下這樣循下來已經知道,
                            #window是Tk()主視窗模組,所以他針對該主視窗模組進行configure指令
                            #那主視窗模組用configure指令是用來針對該window變數名稱的Tk()主視窗模組做背景顏色的
                            #替換,括號裡的bg就是(background)之意,所以就是使用背景顏色為灰色!
lb1=s.Label(window,text="大獎",bg="#A52A2A",width=10,height=1,font=("標楷體",12))
lb2=s.Label(window,text="貳獎",bg="#A52A2A",width=10,height=1,font=("標楷體",12))
lb3=s.Label(window,text="其餘獎",bg="#A52A2A",width=10,height=1,font=("標楷體",12))
lb11=s.Label(window,text="X-MAS PSG-1",bg="#FFD700",width=11,height=1,font=("標楷體",12))
lb21=s.Label(window,text="PSG-1",bg="#C0C0C0",width=11,height=1,font=("標楷體",12))
lb31=s.Label(window,text="武器增加C,D",bg="#BDB76B",width=11,height=1,font=("標楷體",12))
lb32=s.Label(window,text="點數SP增加",bg="#BDB76B",width=11,height=1,font=("標楷體",12))
lb33=s.Label(window,text="經驗值加倍",bg="#BDB76B",width=11,height=1,font=("標楷體",12))
lb34=s.Label(window,text="隨機人物1個1天",bg="#BDB76B",width=14,height=1,font=("標楷體",12))
lb0=s.Label(window,text="Cash "+str(me)+"/250",bg="#808080",width=12,height=2,font=("標楷體",12))
bt1=s.Button(window,text="Start",width=10,command=s1) #當我按下此Button時,bt1就會觸發他得Button裡的command=s1,
                                                      #這時候s1函數名稱由下至上找def遞迴函數,找到相同函數名稱就函數名稱對該函數名稱
                                                      #然後符合就進入def遞迴函數
lb1.place(x=20,y=40)
lb2.place(x=20,y=120)
lb3.place(x=20,y=200)
lb11.place(x=20,y=75)
lb21.place(x=20,y=155)
lb31.place(x=20,y=235)
lb32.place(x=20,y=270)
lb33.place(x=20,y=305)
lb34.place(x=20,y=340)
lb0.place(x=200,y=25)
bt1.place(x=310,y=30)
window.mainloop()
#貳獎與參加獎的點數.
#n=random.randint(1,12)
#如果中1->得大獎X-MAS PSG-1 1天
#     2->得貳獎PSG-1 3天
#     3->得貳獎PSG-1 1天
#     4->得其餘獎點數SP增加 1天
#     5->得其餘獎經驗值加倍 3天
#     6->得其餘獎武器增加C,D 3天
#     7->得貳獎PSG-1 3天
#     8->得其餘獎經驗值加倍 1天
#     9->得其餘獎隨機人物1個1天
#    10->得其餘獎武器增加C,D 1天
#    11->得其餘獎點數SP增加 3天
#    12->得其餘獎隨機人物1個1天                     