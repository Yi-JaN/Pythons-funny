import tkinter as s #此視窗內建套組我用s做簡稱
import matplotlib.pyplot as plt #此數據資料視覺圖內建套組我用plt做簡稱
import random as rd #此亂數內建套組我用rd做簡稱
def s1() :
    global lbs1,lbs2,lbs3,lbs4,lbs5,lbs6,lbs7,lbs8,list1lb2,list1eny1              
    windows1=s.Tk()
    windows1.title("幽默冷笑話類")
    windows1.geometry("550x300+250+300")
    lbs1=s.Label(windows1,text="1.鯊魚吃了綠豆(猜食物)➠綠豆沙")
    lbs2=s.Label(windows1,text="2.醬油的哥哥是誰？➠醬油膏(台語諧音：豆油哥)")
    lbs3=s.Label(windows1,text="3.黑頭髮有什麼好處？➠不怕曬黑")
    lbs4=s.Label(windows1,text="4.一口井、一杯茶、兩個杯子(猜職業)➠警察伯伯 (井茶杯杯)")
    lbs5=s.Label(windows1,text="5.當醫生說你的病沒希望時，該怎麼辦？➠換一個醫生")
    lbs6=s.Label(windows1,text="6.小孩子跌倒(猜成語)➠馬馬虎虎(媽媽撫撫)")
    lbs7=s.Label(windows1,text="7.什麼車最多燈？➠垃圾車(因為它會一邊放音樂：燈燈燈燈燈燈燈~)")
    lbs8=s.Label(windows1,text="8.請問iPhone在哪個大學最難用？➠南華科技大學(難滑科技大學)")
    list1lb1=s.Label(windows1,text="/3") #lblist11的label物件指令是總共頁數
    list1eny1=s.Entry(windows1,width=5) #list1eny1的entry物件指令是輸入你要的頁數
    list1eny1.insert(0,"1") #list1eny1剛生成出來時然後馬上entry物件指令統一設定為第一頁，因為點下去開啟此視窗時，是要
                            #馬上當前呈現就是直接第一頁的內容，所以這裡就用insert()新增指令為他設定為第一頁
    bts1=s.Button(windows1,text="選擇頁數",width=10,command=s11)
    list1lb2=s.Label(windows1,text="1",bg="#737373") #bg參數是自帶意思參數，為背景顏色參數，而該參數可用顏色碼跟輸入顏色做呈現，而我選擇前者
    lbs1.place(x=10,y=10)
    lbs2.place(x=10,y=40)
    lbs3.place(x=10,y=70)
    lbs4.place(x=10,y=100)
    lbs5.place(x=10,y=130)
    lbs6.place(x=10,y=160)
    lbs7.place(x=10,y=190)
    lbs8.place(x=10,y=220)
    list1lb1.place(x=280,y=273)
    list1eny1.place(x=230,y=273)
    bts1.place(x=320,y=270)
    list1lb2.place(x=537,y=279)
    windows1.mainloop()

def s2() :
    global lbss1,lbss2,lbss3,lbss4,lbss5,lbss6,lbss7,lbss8,list2eny1,list2lb2            
    windows2=s.Tk()
    windows2.title("食物與水果類")
    windows2.geometry("700x300+350+300")
    lbss1=s.Label(windows2,text="1.一個婆婆園中站，身上掛滿小雞蛋，又有紅來又有綠，既好吃來又好看(猜食物)➠棗樹")
    lbss2=s.Label(windows2,text="2.小刺蝟，毛外套，脫了外套露紫袍，袍裏套着紅絨襖，襖裏睡個小寶寶(猜食物)➠栗子")
    lbss3=s.Label(windows2,text="3.不是蔥不是蒜，一層一層裹紫緞，說蔥比蔥長得矮，像蒜就是不分瓣(猜蔬菜)➠洋蔥")
    lbss4=s.Label(windows2,text="4.兄弟七八個，圍着柱子坐，大家一分家，衣服就扯破(猜蔬菜)➠蒜")
    lbss5=s.Label(windows2,text="5.白白一片似雪花，落下水裏不見(猜食物)➠鹽")
    lbss6=s.Label(windows2,text="6.白牀鋪，黃帳子(猜食物)➠桂圓")
    lbss7=s.Label(windows2,text="7.白胖娃娃泥裏臥，腰身細細心眼多(猜食物)➠藕")
    lbss8=s.Label(windows2,text="8.白胖胖，四方方，一塊一塊擺桌上，能做菜，能做湯，常常吃它有營養(猜食物)➠豆腐")
    list2lb1=s.Label(windows2,text="/3")
    list2eny1=s.Entry(windows2,width=5)
    list2eny1.insert(0,"1")
    btss1=s.Button(windows2,text="選擇頁數",width=10,command=s21)
    list2lb2=s.Label(windows2,text="1",bg="#737373")
    lbss1.place(x=10,y=10)
    lbss2.place(x=10,y=40)
    lbss3.place(x=10,y=70)
    lbss4.place(x=10,y=100)
    lbss5.place(x=10,y=130)
    lbss6.place(x=10,y=160)
    lbss7.place(x=10,y=190)
    lbss8.place(x=10,y=220)
    list2lb1.place(x=350,y=273)
    list2eny1.place(x=300,y=273)
    btss1.place(x=380,y=270)
    list2lb2.place(x=687,y=279)
    windows2.mainloop()

def s3() :
    global lbsss1,lbsss2,lbsss3,lbsss4,lbsss5,lbsss6,lbsss7,lbsss8,list3eny1,list3lb2        
    windows3=s.Tk()
    windows3.title("文學造詣")
    windows3.geometry("550x300+400+300")
    lbsss1=s.Label(windows3,text="1.2+6(猜一字)➠積")
    lbsss2=s.Label(windows3,text="2.242÷22(猜一字)➠墑")
    lbsss3=s.Label(windows3,text="3.4個人搬個木頭(猜一字)➠傑")
    lbsss4=s.Label(windows3,text="4.一人(猜一字)➠大")
    lbsss5=s.Label(windows3,text="5.一人一張口，下面長隻手(猜一字)➠拿")
    lbsss6=s.Label(windows3,text="6.一人比兩人高(猜一字)➠眾")
    lbsss7=s.Label(windows3,text="7.一人在內(猜一字)➠肉")
    lbsss8=s.Label(windows3,text="8.一人挑兩小人(猜一字)➠夾")
    list3lb1=s.Label(windows3,text="/4")
    list3eny1=s.Entry(windows3,width=5)
    list3eny1.insert(0,"1")
    btsss1=s.Button(windows3,text="選擇頁數",width=10,command=s31)
    list3lb2=s.Label(windows3,text="1",bg="#737373")
    lbsss1.place(x=10,y=10)
    lbsss2.place(x=10,y=40)
    lbsss3.place(x=10,y=70)
    lbsss4.place(x=10,y=100)
    lbsss5.place(x=10,y=130)
    lbsss6.place(x=10,y=160)
    lbsss7.place(x=10,y=190)
    lbsss8.place(x=10,y=220)
    list3lb1.place(x=280,y=273)
    list3eny1.place(x=230,y=273)
    btsss1.place(x=320,y=270)
    list3lb2.place(x=537,y=279)
    windows3.mainloop()

def s4() :
    global lbssss1,lbssss2,lbssss3,lbssss4,lbssss5,lbssss6,lbssss7,lbssss8,list4eny1,list4lb2            
    windows4=s.Tk()
    windows4.title("猜數字類")
    windows4.geometry("550x300+450+300")
    lbssss1=s.Label(windows4,text="1.一來就千(猜數字國字)➠十")
    lbssss2=s.Label(windows4,text="2.八個螞蟻擡棍棍，一個螞蟻棍上昆(猜數字國字)➠六")
    lbssss3=s.Label(windows4,text="3.三與三，嘴對嘴(猜數字)➠8")
    lbssss4=s.Label(windows4,text="4.旭日東昇(猜數字國字)➠九")
    lbssss5=s.Label(windows4,text="5.兩隻鳥兒對頭飛，一隻瘦來一隻肥(猜數字國字)➠八")
    lbssss6=s.Label(windows4,text="6.除了2還是2(猜數字)➠4")
    lbssss7=s.Label(windows4,text="7.添一筆，增百倍，減一筆，少九成(猜數字國字)➠十")
    lbssss8=s.Label(windows4,text="8.棍子打棒球(猜數字)➠10")
    list4lb1=s.Label(windows4,text="/2")
    list4eny1=s.Entry(windows4,width=5)
    list4eny1.insert(0,"1")
    btssss1=s.Button(windows4,text="選擇頁數",width=10,command=s41)
    list4lb2=s.Label(windows4,text="1",bg="#737373")
    lbssss1.place(x=10,y=10)
    lbssss2.place(x=10,y=40)
    lbssss3.place(x=10,y=70)
    lbssss4.place(x=10,y=100)
    lbssss5.place(x=10,y=130)
    lbssss6.place(x=10,y=160)
    lbssss7.place(x=10,y=190)
    lbssss8.place(x=10,y=220)
    list4lb1.place(x=280,y=273)
    list4eny1.place(x=230,y=273)
    btssss1.place(x=320,y=270)
    list4lb2.place(x=537,y=279)
    windows4.mainloop()

def s5() :
    global lbsssss1,lbsssss2,lbsssss3,lbsssss4,lbsssss5,lbsssss6,lbsssss7,lbsssss8,list5eny1,list5lb2            
    windows5=s.Tk()
    windows5.title("物品跟用品及工具類")
    windows5.geometry("700x300+500+300")
    lbsssss1=s.Label(windows5,text="1.一匹馬兒兩人騎，這邊高來那邊低， 雖然馬兒不會跑，兩人騎着笑嘻嘻(猜一物)➠蹺蹺板")
    lbsssss2=s.Label(windows5,text="2.一匹馬兒真正好，沒有尾巴沒有腳，不喝水來不吃草，騎上它就滿街跑唱(猜一物)➠自行車")
    lbsssss3=s.Label(windows5,text="3.一天過去，脫件衣裳，一年過去，全身脫光(猜一物)➠日曆")
    lbsssss4=s.Label(windows5,text="4.一位公公精神好，從小到老不睡覺。身體輕，勁不小，左推右推推不倒(猜一物)➠不倒翁")
    lbsssss5=s.Label(windows5,text="5.一物生得巧，地位比人高。戴上御風寒，脫下有禮貌(猜一物)➠帽子")
    lbsssss6=s.Label(windows5,text="6.一物參個口，你有我也有，有他不怎樣，無他就現醜(猜一物)➠褲子")
    lbsssss7=s.Label(windows5,text="7. 一個大肚皮，生來怪脾氣， 不打不做聲，越打越歡喜(猜一物)➠鼓")
    lbsssss8=s.Label(windows5,text="8.一個小兒郎，每天站桌上。肚裏滾滾熱，肚皮冰冰涼。一個大耳朵，穿件花衣裳(猜一物)➠暖水瓶")
    list5lb1=s.Label(windows5,text="/3")
    list5eny1=s.Entry(windows5,width=5)
    list5eny1.insert(0,"1")
    btsssss1=s.Button(windows5,text="選擇頁面",width=10,command=s51)
    list5lb2=s.Label(windows5,text="1",bg="#737373")
    lbsssss1.place(x=10,y=10)
    lbsssss2.place(x=10,y=40)
    lbsssss3.place(x=10,y=70)
    lbsssss4.place(x=10,y=100)
    lbsssss5.place(x=10,y=130)
    lbsssss6.place(x=10,y=160)
    lbsssss7.place(x=10,y=190)
    lbsssss8.place(x=10,y=220)
    list5lb1.place(x=350,y=273)
    list5eny1.place(x=300,y=273)
    btsssss1.place(x=380,y=270)
    list5lb2.place(x=687,y=279)
    windows5.mainloop()

def firststart() :
    global firstquestion,start,hintq1,hintq2,imok
    start=1 #當我進入此這裡，代表觸碰了開始/下一題的按鈕，然後藉由他身上的command參數來到這邊，1為代表要開始跟下一題，同時也代表1是目前"開始這一輪"的計分
    imok=1 #當我run到這一行代表待會要出新題目，那imok會給1，意思是新題目會有1次確定交送答案審查機會，這樣該新題目答對才算分，之後新題目不管答對或錯都會imok歸0，代表暫無確定交送答案審查機會，怕防止同一題答對出現刷分現象
    if start==1 : #如果start是1，代表"開始這一輪"了，那就進去抽題目
        lb4.configure(text="提示1") #開始或下一題後提示測試部分用掉
        lb5.configure(text="提示2") #開始或下一題後提示測試部分用掉
        answerr.configure(text="A: ")
        eny1.delete(0,"end")
        hintq1=0 #提示1跟提示2先歸0，代表要開始或者要下一題，統一run到這歸0
        hintq2=0
        firstquestion=rd.randint(1,114) #不管是剛開始還是正要下一題，都要隨機抽題目
        if firstquestion==1 :
            lb2.configure(text="鯊魚吃了綠豆(猜食物)")
            lb3.configure(text="")
        elif firstquestion==2 :
            lb2.configure(text="醬油的哥哥是誰？")
            lb3.configure(text="")
        elif firstquestion==3 :
            lb2.configure(text="黑頭髮有什麼好處？")
            lb3.configure(text="")
        elif firstquestion==4 :
            lb2.configure(text="一口井、一杯茶、兩個杯子(猜職業)")
            lb3.configure(text="")
        elif firstquestion==5 :
            lb2.configure(text="當醫生說你的病沒希望時，該怎麼辦？")
            lb3.configure(text="")   
        elif firstquestion==6 :
            lb2.configure(text="小孩子跌倒(猜成語)")
            lb3.configure(text="")
        elif firstquestion==7 :
            lb2.configure(text="什麼車最多燈？")
            lb3.configure(text="")
        elif firstquestion==8 :
            lb2.configure(text="請問iPhone在哪個大學最難用？")
            lb3.configure(text="")
        elif firstquestion==9 :
            lb2.configure(text="「3」在路上走呀走，翻了兩次跟斗(猜成語)")
            lb3.configure(text="")
        elif firstquestion==10 :
            lb2.configure(text="4個人在屋子打麻將，警察來了為什麼帶走5個人？")
            lb3.configure(text="")
        elif firstquestion==11 :
            lb2.configure(text="Costco鬧鬼(猜成語)")
            lb3.configure(text="")
        elif firstquestion==12 :
            lb2.configure(text="Hello Kitty賣光光(猜台灣地名)")
            lb3.configure(text="")
        elif firstquestion==13 :
            lb2.configure(text="ㄊㄞˊ(猜一個古代人名)")
            lb3.configure(text="")
        elif firstquestion==14 :
            lb2.configure(text="他走了的英文怎麼說？")
            lb3.configure(text="")
        elif firstquestion==15 :
            lb2.configure(text="冬瓜、西瓜、南瓜都能吃，什麼瓜不能吃？")
            lb3.configure(text="")
        elif firstquestion==16 :
            lb2.configure(text="只騙中年人(猜成語)")
            lb3.configure(text="")
        elif firstquestion==17 :
            lb2.configure(text="打什麼東西，不必花力氣？")
            lb3.configure(text="")
        elif firstquestion==18 :
            lb2.configure(text="玉米燙頭髮變成什麼(猜食物)")
            lb3.configure(text="")
        elif firstquestion==19 :
            lb2.configure(text="一塊錢可以買幾頭牛？")
            lb3.configure(text="")
        elif firstquestion==20 :
            lb2.configure(text="真正的豬喝什麼飲料？")
            lb3.configure(text="")
        elif firstquestion==21 :
            lb2.configure(text="真實的山，冒充的海(猜成語)")
            lb3.configure(text="")
        elif firstquestion==22 :
            lb2.configure(text="一頭豬說：加油！(猜食物)")
            lb3.configure(text="")
        elif firstquestion==23 :
            lb2.configure(text="馬克，約翰，湯姆，誰可以讓比薩斜塔不倒下來？")
            lb3.configure(text="")
        elif firstquestion==24 :
            lb2.configure(text="被人家放了鴿子還很高興的是誰？")
            lb3.configure(text="")
        elif firstquestion==25 :
            lb2.configure(text="一個婆婆園中站，身上掛滿小雞蛋，又有紅來又有綠，既好吃")
            lb3.configure(text="來又好看(猜食物)")
        elif firstquestion==26 :
            lb2.configure(text="小刺蝟，毛外套，脫了外套露紫袍，袍裏套着紅絨襖，襖裏睡")
            lb3.configure(text="個小寶寶(猜食物)")
        elif firstquestion==27 :
            lb2.configure(text="不是蔥不是蒜，一層一層裹紫緞，說蔥比蔥長得矮，像蒜就是")
            lb3.configure(text="不分瓣(猜蔬菜)")
        elif firstquestion==28 :
            lb2.configure(text="兄弟七八個，圍着柱子坐，大家一分家，衣服就扯破(猜蔬菜)")
            lb3.configure(text="")
        elif firstquestion==29 :
            lb2.configure(text="白白一片似雪花，落下水裏不見(猜食物)")
            lb3.configure(text="")
        elif firstquestion==30 :
            lb2.configure(text="白牀鋪，黃帳子(猜食物)")
            lb3.configure(text="")
        elif firstquestion==31 :
            lb2.configure(text="白胖娃娃泥裏臥，腰身細細心眼多(猜食物)")
            lb3.configure(text="")
        elif firstquestion==32 :
            lb2.configure(text="白胖胖，四方方，一塊一塊擺桌上，能做菜，能做湯，常常吃")
            lb3.configure(text="它有營養(猜食物)")
        elif firstquestion==33 :
            lb2.configure(text="白糖梅子真稀奇(猜食物)")
            lb3.configure(text="")
        elif firstquestion==34 :
            lb2.configure(text="百姐妹，千姐妹，同床睡，各蓋被(猜水果)")
            lb3.configure(text="")
        elif firstquestion==35 :
            lb2.configure(text="把把綠傘土裏插，條條紫藤地上爬，地上長葉不開花，地下結")
            lb3.configure(text="串大甜瓜(猜食物)")
        elif firstquestion==36 :
            lb2.configure(text="身子長，個不大，遍體長着小疙瘩，有人見了皺眉頭，有人見")
            lb3.configure(text="了樂開花(猜蔬菜)")
        elif firstquestion==37 :
            lb2.configure(text="身材瘦瘦個兒高，葉兒細細披綠袍，別看樣子像青蒿，香氣撲")
            lb3.configure(text="鼻味兒好(猜蔬菜)")
        elif firstquestion==38 :
            lb2.configure(text="身體圓圓沒有毛，不是桔子不是桃，雲裏霧裏過幾夜，脫去綠")
            lb3.configure(text="衣換紅袍(猜水果)")
        elif firstquestion==39 :
            lb2.configure(text="來自水中，卻怕水衝，回到水裏，無影無蹤(猜食物)")
            lb3.configure(text="")
        elif firstquestion==40 :
            lb2.configure(text="味道甜甜營養多，誰說無花只結果，其實花開密又小，切莫被")
            lb3.configure(text="名所迷惑(猜食物)")
        elif firstquestion==41 :
            lb2.configure(text="狀如蘑菇一珍寶，當年白蛇將它盜，其實是味好草藥，滋補健")
            lb3.configure(text="身價值高(猜食物)")
        elif firstquestion==42 :
            lb2.configure(text="青皮包白肉，像個大枕頭，莫聽名字冷，熱天菜場有(猜蔬菜)")
            lb3.configure(text="")
        elif firstquestion==43 :
            lb2.configure(text="春穿綠衣秋黃袍，頭兒彎彎垂珠寶，從幼到老難離水，不洗澡")
            lb3.configure(text="來只泡腳(猜食物)")
        elif firstquestion==44 :
            lb2.configure(text="紅口袋，綠口袋，有人怕，有人愛，愛它是樣好小菜，怕它吃")
            lb3.configure(text="到嘴裏眼淚來(猜蔬菜)")
        elif firstquestion==45 :
            lb2.configure(text="紅公雞，綠公雞，身子鑽在泥底下，你要捉住它，揪住尾巴用")
            lb3.configure(text="力拔(猜蔬菜)")
        elif firstquestion==46 :
            lb2.configure(text="紅嘴綠鸚哥，吃了營養多(猜蔬菜)")
            lb3.configure(text="")
        elif firstquestion==47 :
            lb2.configure(text="個兒小小，頭尾尖尖，初嘗皺眉，再吃開顏(猜食物)")
            lb3.configure(text="")
        elif firstquestion==48 :
            lb2.configure(text="脫了紅袍子，是個白胖子，去了白胖子，剩個黑丸子(猜水果)")
            lb3.configure(text="")
        elif firstquestion==49 :
            lb2.configure(text="2+6(猜一字)")
            lb3.configure(text="")
        elif firstquestion==50 :
            lb2.configure(text="242÷22(猜一字)")
            lb3.configure(text="")
        elif firstquestion==51 :
            lb2.configure(text="4個人搬個木頭(猜一字)")
            lb3.configure(text="")
        elif firstquestion==52 :
            lb2.configure(text="一人(猜一字)")
            lb3.configure(text="")
        elif firstquestion==53 :
            lb2.configure(text="一人一張口，下面長隻手(猜一字)")
            lb3.configure(text="")
        elif firstquestion==54 :
            lb2.configure(text="一人比兩人高(猜一字)")
            lb3.configure(text="")
        elif firstquestion==55 :
            lb2.configure(text="一人在內(猜一字)")
            lb3.configure(text="")
        elif firstquestion==56 :
            lb2.configure(text="一人挑兩小人(猜一字)")
            lb3.configure(text="")
        elif firstquestion==57 :
            lb2.configure(text="一口吃掉牛尾巴(猜一字)")
            lb3.configure(text="")
        elif firstquestion==58 :
            lb2.configure(text="一口咬去多半截(猜一字)")
            lb3.configure(text="")
        elif firstquestion==59 :
            lb2.configure(text="一口咬定(猜一字)")
            lb3.configure(text="")
        elif firstquestion==60 :
            lb2.configure(text="一大二小(猜一字)")
            lb3.configure(text="")
        elif firstquestion==61 :
            lb2.configure(text="一勾心月伴三星(猜一字)")
            lb3.configure(text="")
        elif firstquestion==62 :
            lb2.configure(text="一心一意(猜一字)")
            lb3.configure(text="")
        elif firstquestion==63 :
            lb2.configure(text="一心向上(猜一字)")
            lb3.configure(text="")
        elif firstquestion==64 :
            lb2.configure(text="一心依賴實為惰(猜一字)")
            lb3.configure(text="")
        elif firstquestion==65 :
            lb2.configure(text="一斗米(猜一字)")
            lb3.configure(text="")
        elif firstquestion==66 :
            lb2.configure(text="一月一日非今天(猜一字)")
            lb3.configure(text="")
        elif firstquestion==67 :
            lb2.configure(text="一月七日(猜一字)")
            lb3.configure(text="")
        elif firstquestion==68 :
            lb2.configure(text="一加一(猜一字)")
            lb3.configure(text="")
        elif firstquestion==69 :
            lb2.configure(text="一加一不是二(猜一字)")
            lb3.configure(text="")
        elif firstquestion==70 :
            lb2.configure(text="一半兒(猜一字)")
            lb3.configure(text="")
        elif firstquestion==71 :
            lb2.configure(text="一字十三點，難在如何點(猜一字)")
            lb3.configure(text="")
        elif firstquestion==72 :
            lb2.configure(text="一字六筆無豎橫，同心同德力無窮(猜一字)")
            lb3.configure(text="")
        elif firstquestion==73 :
            lb2.configure(text="一字生得巧，四面八隻腳(猜一字)")
            lb3.configure(text="")
        elif firstquestion==74 :
            lb2.configure(text="一百減一(猜一字)")
            lb3.configure(text="")
        elif firstquestion==75 :
            lb2.configure(text="一走就帶千軍(猜一字)")
            lb3.configure(text="")
        elif firstquestion==76 :
            lb2.configure(text="一來再來(猜一字)")
            lb3.configure(text="")
        elif firstquestion==77 :
            lb2.configure(text="一來就有徒弟(猜一字)")
            lb3.configure(text="")
        elif firstquestion==78 :
            lb2.configure(text="一夜又一夜(猜一字)")
            lb3.configure(text="")
        elif firstquestion==79 :
            lb2.configure(text="一柱擎天(猜一字)")
            lb3.configure(text="")
        elif firstquestion==80 :
            lb2.configure(text="一流水準(猜一字)")
            lb3.configure(text="")
        elif firstquestion==81 :
            lb2.configure(text="一來就千(猜數字國字)")
            lb3.configure(text="")
        elif firstquestion==82 :
            lb2.configure(text="八個螞蟻擡棍棍，一個螞蟻棍上昆(猜數字國字)")
            lb3.configure(text="")
        elif firstquestion==83 :
            lb2.configure(text="三與三，嘴對嘴(猜數字)")
            lb3.configure(text="")
        elif firstquestion==84 :
            lb2.configure(text="旭日東昇(猜數字國字)")
            lb3.configure(text="")
        elif firstquestion==85 :
            lb2.configure(text="兩隻鳥兒對頭飛，一隻瘦來一隻肥(猜數字國字)")
            lb3.configure(text="")
        elif firstquestion==86 :
            lb2.configure(text="除了2還是2(猜數字)")
            lb3.configure(text="")
        elif firstquestion==87 :
            lb2.configure(text="添一筆，增百倍，減一筆，少九成(猜數字國字)")
            lb3.configure(text="")
        elif firstquestion==88 :
            lb2.configure(text="棍子打棒球(猜數字)")
            lb3.configure(text="")
        elif firstquestion==89 :
            lb2.configure(text="語言不通難開口(猜數字國字)")
            lb3.configure(text="")
        elif firstquestion==90 :
            lb2.configure(text="數字雖小，卻在百萬之上(猜數字國字)")
            lb3.configure(text="")
        elif firstquestion==91 :
            lb2.configure(text="一匹馬兒兩人騎，這邊高來那邊低， 雖然馬兒不會跑，兩人騎")
            lb3.configure(text="着笑嘻嘻(猜一物)")
        elif firstquestion==92 :
            lb2.configure(text="一匹馬兒真正好，沒有尾巴沒有腳，不喝水來不吃草，騎上它")
            lb3.configure(text="就滿街跑唱(猜一物)")
        elif firstquestion==93 :
            lb2.configure(text="一天過去，脫件衣裳，一年過去，全身脫光(猜一物)")
            lb3.configure(text="")
        elif firstquestion==94 :
            lb2.configure(text="一位公公精神好，從小到老不睡覺。身體輕，勁不小，左推右")
            lb3.configure(text="推推不倒(猜一物)")
        elif firstquestion==95 :
            lb2.configure(text="一物生得巧，地位比人高。戴上御風寒，脫下有禮貌(猜一物)")
            lb3.configure(text="")
        elif firstquestion==96 :
            lb2.configure(text="一物參個口，你有我也有，有他不怎樣，無他就現醜(猜一物)")
            lb3.configure(text="")
        elif firstquestion==97 :
            lb2.configure(text="一個大肚皮，生來怪脾氣， 不打不做聲，越打越歡喜(猜一物)")
            lb3.configure(text="")
        elif firstquestion==98 :
            lb2.configure(text="一個小兒郎，每天站桌上。肚裏滾滾熱，肚皮冰冰涼。一個大")
            lb3.configure(text="耳朵，穿件花衣裳(猜一物)")
        elif firstquestion==99 :
            lb2.configure(text="一個小黑人，跳進洗澡盆，越洗越不凈，長人變短人(猜一物)")
            lb3.configure(text="")
        elif firstquestion==100 :
            lb2.configure(text="一個小碗尾巴長，能盛飯菜能盛湯。盛上又倒了，倒了再盛上(猜")
            lb3.configure(text="一物)")
        elif firstquestion==101 :
            lb2.configure(text="一個瓜，腰上掛，抽了筋，就開花，消滅敵人要用它(猜一物)")
            lb3.configure(text="")
        elif firstquestion==102 :
            lb2.configure(text="一個南瓜兩頭兒空，肚裏開花放光明，有瓜沒葉兒高高掛，照")
            lb3.configure(text="得面前一片紅(猜一物)")
        elif firstquestion==103 :
            lb2.configure(text="一個娃娃小不點，一件紅襖身上穿，香火把它的辮子點，大叫")
            lb3.configure(text="一聲飛上天(猜一物)")
        elif firstquestion==104 :
            lb2.configure(text="一個風箱真奇怪，一拉它就唱起來(猜一物)")
            lb3.configure(text="")
        elif firstquestion==105 :
            lb2.configure(text="一座橋，地上架，走着上去坐着下(猜一物)")
            lb3.configure(text="")
        elif firstquestion==106 :
            lb2.configure(text="一根小木棒，安個彎月亮。秋天收莊稼，請它來幫忙唱(猜一物)")
            lb3.configure(text="")
        elif firstquestion==107 :
            lb2.configure(text="一根小棍兒，頂個圓粒兒，小孩兒玩它，容易出事兒(猜一物)")
            lb3.configure(text="")
        elif firstquestion==108 :
            lb2.configure(text="一根竹管二尺長，開了七個小圓窗， 對準一個小窗口，吹陣")
            lb3.configure(text="風就把歌唱(猜一物)")
        elif firstquestion==109 :
            lb2.configure(text="一根柱子好些樑，沒有門窗沒有牆，好象一座小亭子，用它擋")
            lb3.configure(text="雨遮太陽(猜一物)")
        elif firstquestion==110 :
            lb2.configure(text="一條怪牛，兩條圓腿，騎他肚上，抓他雙角(猜一物)")
            lb3.configure(text="")
        elif firstquestion==111 :
            lb2.configure(text="一間小藥房，藥品裡面藏。房子塗白色，十字畫中央(猜一物)")
            lb3.configure(text="")
        elif firstquestion==112 :
            lb2.configure(text="一間房子扁又長，上邊開了許多窗，用嘴吹進一陣風，好聽的")
            lb3.configure(text="音樂多響亮(猜一物)")
        elif firstquestion==113 :
            lb2.configure(text="一樣東西亮晶晶，又光又硬又透明，工人叔叔造出來，它的用")
            lb3.configure(text="處數不清(猜一物)")
        elif firstquestion==114 :
            lb2.configure(text="一雙玉燕靠地飛，早上出門夜裏歸(猜一物)")
            lb3.configure(text="")

def clears() :
    global start,user,firstquestion,imok
    start=0 #這裡同時就相當於清除的概念，所以首先控制"開始"猜燈謎的變數名稱就先歸0，代表清除不動作
    user=0 #清除總分數的變數名稱，變為0
    imok=0 #防止確定答案的變數名稱歸0，等下一次出題
    firstquestion=0 #清除電腦隨機抽出的題目，變為0，代表什麼題目都不是的狀態
    lb2.configure(text="") #lb2跟lb3利用configure指令，把自身text變成""，代表有清除之意
    lb3.configure(text="")
    lb4.configure(text="提示1") #lb4跟lb5利用configure指令,把自身text變成"提示1"跟"提示2"，代表
    lb5.configure(text="提示2") #清除並回歸到當初最一開始要開始前的視窗狀態模樣顯現
    scores.configure(text="0") #scores利用configure指令，把自身text變成"0"，代表總分丟到label物件指令顯現為0，同時代表總分目前為0
    answerr.configure(text="A: ")
    eny1.delete(0,"end")
            
def hint1() :
    global start,firstquestion,hintq1
    if start==1 : #如果start是1就進去，代表是"開始這一輪"猜燈謎的狀態，所以待會進去可以看我現在是哪一題，針對那題給出那題的提示1出來
       if firstquestion==1 : #如果是第一題就進去
           hintq1=1 #hintq1代表提示1，變為1，代表目前用了提示1
           lb4.configure(text="常見喝的飲料") #第一題的提示1顯示出來
       elif firstquestion==2 :
           hintq1=1
           lb4.configure(text="炒菜常用的")
       elif firstquestion==3 :
           hintq1=1
           lb4.configure(text="人的身體方面")
       elif firstquestion==4 :
           hintq1=1
           lb4.configure(text="公家機關")
       elif firstquestion==5 :
           hintq1=1
           lb4.configure(text="下醫醫病，中醫醫心，上醫醫國")
       elif firstquestion==6 :
           hintq1=1
           lb4.configure(text="跌倒小孩子會哭，所以...?")
       elif firstquestion==7 :
           hintq1=1
           lb4.configure(text="每天固定時間會來幫忙幹嘛...?做甚麼..?")
       elif firstquestion==8 :
           hintq1=1
           lb4.configure(text="教育機構(縮小範圍至科技大學)")
       elif firstquestion==9 :
           hintq1=1
           lb4.configure(text="四個字成語")
       elif firstquestion==10 :
           hintq1=1
           lb4.configure(text="提示1到4個字:因為他們，然後這是有用到數學的題目")
       elif firstquestion==11 :
           hintq1=1
           lb4.configure(text="四個字成語")
       elif firstquestion==12 :
           hintq1=1
           lb4.configure(text="他是一個有景觀特色之稱的地方")
       elif firstquestion==13 :
           hintq1=1
           lb4.configure(text="很多人都知道的中國民間傳說故事")
       elif firstquestion==14 :
           hintq1=1
           lb4.configure(text="家具賣場(很多人都熟知的)")
       elif firstquestion==15 :
           hintq1=1
           lb4.configure(text="罵一個人貶低一個人常用的詞(兩個字)")
       elif firstquestion==16 :
           hintq1=1
           lb4.configure(text="四個字成語，跟小孩及老人有關的成語")
       elif firstquestion==17 :
           hintq1=1
           lb4.configure(text="學生最愛做的事情")
       elif firstquestion==18 :
           hintq1=1
           lb4.configure(text="三個字的食物(偏零食類)")
       elif firstquestion==19 :
           hintq1=1
           lb4.configure(text="三個字答案，但是這三個字答案跟某個成語有關")
       elif firstquestion==20 :
           hintq1=1
           lb4.configure(text="題目裡的豬用諧音話來念")
       elif firstquestion==21 :
           hintq1=1
           lb4.configure(text="四個字成語，跟吃的有關")
       elif firstquestion==22 :
           hintq1=1
           lb4.configure(text="甜甜的食品")
       elif firstquestion==23 :
           hintq1=1
           lb4.configure(text="跟一位美國男子演員有關")
       elif firstquestion==24 :
           hintq1=1
           lb4.configure(text="因為放鴿子不是指已經定下了約會而沒有赴約的行為")
       elif firstquestion==25 :
           hintq1=1
           lb4.configure(text="兩個字食物")
       elif firstquestion==26 :
           hintq1=1
           lb4.configure(text="(兩個字食物)用砂糖炒很好吃")
       elif firstquestion==27 :
           hintq1=1
           lb4.configure(text="(兩個字)會很想哭")
       elif firstquestion==28 :
           hintq1=1
           lb4.configure(text="(一個字)很多人聞會不喜歡的")
       elif firstquestion==29 :
           hintq1=1
           lb4.configure(text="(一個字)調味料，很早時期就有的")
       elif firstquestion==30 :
           hintq1=1
           lb4.configure(text="(兩個字)可用成茶來喝解憂慮")
       elif firstquestion==31 :
           hintq1=1
           lb4.configure(text="(一個字)可生吃也可熟吃")
       elif firstquestion==32 :
           hintq1=1
           lb4.configure(text="(兩個字)蛋豆魚肉類")
       elif firstquestion==33 :
           hintq1=1
           lb4.configure(text="(兩個字)字的意思跟節日有關")
       elif firstquestion==34 :
           hintq1=1
           lb4.configure(text="(兩個字)圓體食物")
       elif firstquestion==35 :
           hintq1=1
           lb4.configure(text="(兩個字)熱量不高很常聽到的食物")
       elif firstquestion==36 :
           hintq1=1
           lb4.configure(text="(兩個字)煮熟的樣子不討人喜歡")
       elif firstquestion==37 :
           hintq1=1
           lb4.configure(text="(兩個字)吃了可讓血管放鬆且健康食物")
       elif firstquestion==38 :
           hintq1=1
           lb4.configure(text="(兩個字)水果且中國 日本 韓國 巴西是主要產地")
       elif firstquestion==39 :
           hintq1=1
           lb4.configure(text="(一個字)小小的東西泡在水裡")
       elif firstquestion==40 :
           hintq1=1
           lb4.configure(text="(三個字)")
       elif firstquestion==41 :
           hintq1=1
           lb4.configure(text="(兩個字)屬中醫藥材")
       elif firstquestion==42 :
           hintq1=1
           lb4.configure(text="(兩個字)可變成喝的東西")
       elif firstquestion==43 :
           hintq1=1
           lb4.configure(text="(兩個字)此物主要以水田栽培")
       elif firstquestion==44 :
           hintq1=1
           lb4.configure(text="(兩個字)大家都知道的調味劑")
       elif firstquestion==45 :
           hintq1=1
           lb4.configure(text="(兩個字)家庭常用蔬菜，可煮成菜或湯")
       elif firstquestion==46 :
           hintq1=1
           lb4.configure(text="(兩個字)可炒 做湯 做餡的蔬菜")
       elif firstquestion==47 :
           hintq1=1
           lb4.configure(text="(兩個字)在超市有在賣的XX油")
       elif firstquestion==48 :
           hintq1=1
           lb4.configure(text="(兩個字)甜甜且裡面包有果實")    
       elif firstquestion==49 :
           hintq1=1
           lb4.configure(text="小孩子最常玩的玩具之一的其中一個字")
       elif firstquestion==50 :
           hintq1=1
           lb4.configure(text="箭靶的中心")
       elif firstquestion==51 :
           hintq1=1
           lb4.configure(text="很多人名字裡有的其中一個字")
       elif firstquestion==52 :
           hintq1=1
           lb4.configure(text="平常很常講的一個字")
       elif firstquestion==53 :
           hintq1=1
           lb4.configure(text="牛奶+紅茶")
       elif firstquestion==54 :
           hintq1=1
           lb4.configure(text="此字可以說為大家的意思的字")
       elif firstquestion==55 :
           hintq1=1
           lb4.configure(text="葷的食物")
       elif firstquestion==56 :
           hintq1=1
           lb4.configure(text="投零錢的機器")
       elif firstquestion==57 :
           hintq1=1
           lb4.configure(text="上是牛下是一")
       elif firstquestion==58 :
           hintq1=1
           lb4.configure(text="藝人也可稱為X人")
       elif firstquestion==59 :
           hintq1=1
           lb4.configure(text="台灣有一所國立大學用到的字")
       elif firstquestion==60 :
           hintq1=1
           lb4.configure(text="可簡稱納")
       elif firstquestion==61 :
           hintq1=1
           lb4.configure(text="每個人都有的東西")
       elif firstquestion==62 :
           hintq1=1
           lb4.configure(text="想念之譯")
       elif firstquestion==63 :
           hintq1=1
           lb4.configure(text="一定的意思會用到的字")
       elif firstquestion==64 :
           hintq1=1
           lb4.configure(text="人都會有的一個習慣，多與少罷了")
       elif firstquestion==65 :
           hintq1=1
           lb4.configure(text="十畫筆畫")
       elif firstquestion==66 :
           hintq1=1
           lb4.configure(text="以前有一個朝代的國號")
       elif firstquestion==67 :
           hintq1=1
           lb4.configure(text="人體身上會有的東西，這東西的其中一個字")
       elif firstquestion==68 :
           hintq1=1
           lb4.configure(text="人常見的姓氏")
       elif firstquestion==69 :
           hintq1=1
           lb4.configure(text="國家的最高領導")
       elif firstquestion==70 :
           hintq1=1
           lb4.configure(text="六畫筆畫")
       elif firstquestion==71 :
           hintq1=1
           lb4.configure(text="題目的某兩個字互換")
       elif firstquestion==72 :
           hintq1=1
           lb4.configure(text="許多的意思裡會用到的一個字")
       elif firstquestion==73 :
           hintq1=1
           lb4.configure(text="OOXX")
       elif firstquestion==74 :
           hintq1=1
           lb4.configure(text="題目裡有其中一個字的諧音不同字的字")
       elif firstquestion==75 :
           hintq1=1
           lb4.configure(text="跟古時候打仗時某個職位有關的一個字")
       elif firstquestion==76 :
           hintq1=1
           lb4.configure(text="再")
       elif firstquestion==77 :
           hintq1=1
           lb4.configure(text="老師去一筆畫")
       elif firstquestion==78 :
           hintq1=1
           lb4.configure(text="跟題目的夜有關")
       elif firstquestion==79 :
           hintq1=1
           lb4.configure(text="跟末很像")
       elif firstquestion==80 :
           hintq1=1
           lb4.configure(text="此字左邊是水部")
       elif firstquestion==81 :
           hintq1=1
           lb4.configure(text="某個完美的意思的成語會用到的字")
       elif firstquestion==82 :
           hintq1=1
           lb4.configure(text="我考試及格了")
       elif firstquestion==83 :
           hintq1=1
           lb4.configure(text="嘴對嘴親親")
       elif firstquestion==84 :
           hintq1=1
           lb4.configure(text="此字以他開頭的成語很多")
       elif firstquestion==85 :
           hintq1=1
           lb4.configure(text="在路上很吵的聲音")
       elif firstquestion==86 :
           hintq1=1
           lb4.configure(text="古人說不吉利的音譯")
       elif firstquestion==87 :
           hintq1=1
           lb4.configure(text="進位")
       elif firstquestion==88 :
           hintq1=1
           lb4.configure(text="球棒擊球瞬間的畫面")
       elif firstquestion==89 :
           hintq1=1
           lb4.configure(text="1/2只有一半")
       elif firstquestion==90 :
           hintq1=1
           lb4.configure(text="只有我才是這個國家的領導者")
       elif firstquestion==91 :
           hintq1=1
           lb4.configure(text="一種長方形的小孩子遊戲設施")
       elif firstquestion==92 :
           hintq1=1
           lb4.configure(text="此物是利用自己本人去發動的東西")
       elif firstquestion==93 :
           hintq1=1
           lb4.configure(text="有此物的話，每天都會去做的一件事，花費時間不多")
       elif firstquestion==94 :
           hintq1=1
           lb4.configure(text="古老玩具，裡面是空心殼體")
       elif firstquestion==95 :
           hintq1=1
           lb4.configure(text="穿搭之一的物件")
       elif firstquestion==96 :
           hintq1=1
           lb4.configure(text="人身上經常使用的東西")
       elif firstquestion==97 :
           hintq1=1
           lb4.configure(text="(一個字)可拿來當音樂樂器")
       elif firstquestion==98 :
           hintq1=1
           lb4.configure(text="屬於人的隨身攜帶之一的物品")
       elif firstquestion==99 :
           hintq1=1
           lb4.configure(text="(一個字)此物可以說跟硯台有關")
       elif firstquestion==100 :
           hintq1=1
           lb4.configure(text="屬於手再拿的東西")
       elif firstquestion==101 :
           hintq1=1
           lb4.configure(text="會爆炸的東西")
       elif firstquestion==102 :
           hintq1=1
           lb4.configure(text="晚上點的話會很漂亮")
       elif firstquestion==103 :
           hintq1=1
           lb4.configure(text="結婚 過新年會用到的東西")
       elif firstquestion==104 :
           hintq1=1
           lb4.configure(text="此物歷史要講到過去18世紀歐洲")
       elif firstquestion==105 :
           hintq1=1
           lb4.configure(text="有些公園會有的遊樂設施")
       elif firstquestion==106 :
           hintq1=1
           lb4.configure(text="他是屬於工具類的兩個字物品")
       elif firstquestion==107 :
           hintq1=1
           lb4.configure(text="用此物的話會刷~一聲")
       elif firstquestion==108 :
           hintq1=1
           lb4.configure(text="跟國小的音樂課有關")
       elif firstquestion==109 :
           hintq1=1
           lb4.configure(text="風很大吹此物，此物外表會變形")
       elif firstquestion==110 :
           hintq1=1
           lb4.configure(text="環保 靈活方便")
       elif firstquestion==111 :
           hintq1=1
           lb4.configure(text="紅色十字")
       elif firstquestion==112 :
           hintq1=1
           lb4.configure(text="小型樂器")
       elif firstquestion==113 :
           hintq1=1
           lb4.configure(text="出門大街小巷都會看的到")
       elif firstquestion==114 :
           hintq1=1
           lb4.configure(text="兩個統整為一個")

def hint2() :
    global start,firstquestion,hintq2
    if start==1 :
       if firstquestion==1 :
           hintq2=1
           lb5.configure(text="有綠豆味道在裡面")
       elif firstquestion==2 :
           hintq2=1
           lb5.configure(text="調味用")
       elif firstquestion==3 :
           hintq2=1
           lb5.configure(text="沒了過一段時間又有的")
       elif firstquestion==4 :
           hintq2=1
           lb5.configure(text="四個字，跟題目有關")
       elif firstquestion==5 :
           hintq2=1
           lb5.configure(text="去別的醫院看病")
       elif firstquestion==6 :
           hintq2=1
           lb5.configure(text="媽媽讓小孩不哭")
       elif firstquestion==7 :
           hintq2=1
           lb5.configure(text="燈燈燈燈燈燈燈")
       elif firstquestion==8 :
           hintq2=1
           lb5.configure(text="這地方好難滑")
       elif firstquestion==9 :
           hintq2=1
           lb5.configure(text="跟數字有關")
       elif firstquestion==10 :
           hintq2=1
           lb5.configure(text="被打的人是誰")
       elif firstquestion==11 :
           hintq2=1
           lb5.configure(text="成語意思:美好的事，要經過很多波折才能如願")
       elif firstquestion==12 :
           hintq2=1
           lb5.configure(text="位於台北")
       elif firstquestion==13 :
           hintq2=1
           lb5.configure(text="與梁山伯有關")
       elif firstquestion==14 :
           hintq2=1
           lb5.configure(text="念起來像他走了的台語")
       elif firstquestion==15 :
           hintq2=1
           lb5.configure(text="跟笨蛋之意有關")
       elif firstquestion==16 :
           hintq2=1
           lb5.configure(text="成語之意:有不會欺瞞之意")
       elif firstquestion==17 :
           hintq2=1
           lb5.configure(text="上課時間")
       elif firstquestion==18 :
           hintq2=1
           lb5.configure(text="此物剛開始用的過程會像開花一樣")
       elif firstquestion==19 :
           hintq2=1
           lb5.configure(text="與題目裡的牛有關")
       elif firstquestion==20 :
           hintq2=1
           lb5.configure(text="外國人很印象深刻的東西")
       elif firstquestion==21 :
           hintq2=1
           lb5.configure(text="代表這人家境很好很有錢")
       elif firstquestion==22 :
           hintq2=1
           lb5.configure(text="與可可果實有關")
       elif firstquestion==23 :
           hintq2=1
           lb5.configure(text="有參與昆汀·塔倫提諾的電影")
       elif firstquestion==24 :
           hintq2=1
           lb5.configure(text="一個動物")
       elif firstquestion==25 :
           hintq2=1
           lb5.configure(text="魯迅說過:(一顆是??，另一顆還是??)")
       elif firstquestion==26 :
           hintq2=1
           lb5.configure(text="跑跑卡丁車有一個人物戴眼鏡的角色叫什麼?")
       elif firstquestion==27 :
           hintq2=1
           lb5.configure(text="吃壽喜燒會丟下去的配菜之一")
       elif firstquestion==28 :
           hintq2=1
           lb5.configure(text="嘴巴很臭")
       elif firstquestion==29 :
           hintq2=1
           lb5.configure(text="跟人已經是形影不離的狀態東西")
       elif firstquestion==30 :
           hintq2=1
           lb5.configure(text="可以拿來做成紅棗枸杞茶")
       elif firstquestion==31 :
           hintq2=1
           lb5.configure(text="偏中醫類型的")
       elif firstquestion==32 :
           hintq2=1
           lb5.configure(text="可以跟皮蛋一起做的食材，變成一道菜")
       elif firstquestion==33 :
           hintq2=1
           lb5.configure(text="湯圓")
       elif firstquestion==34 :
           hintq2=1
           lb5.configure(text="帶籽")
       elif firstquestion==35 :
           hintq2=1
           lb5.configure(text="可炸可煮來吃")
       elif firstquestion==36 :
           hintq2=1
           lb5.configure(text="可消暑 降火氣 清心")
       elif firstquestion==37 :
           hintq2=1
           lb5.configure(text="此菜分為本土 西洋型種的菜")
       elif firstquestion==38 :
           hintq2=1
           lb5.configure(text="分為甜跟澀兩種的水果")
       elif firstquestion==39 :
           hintq2=1
           lb5.configure(text="一丟到水裡就會看不見")
       elif firstquestion==40 :
           hintq2=1
           lb5.configure(text="咬下去口感像芝麻且在嘴巴會卡滋卡滋")
       elif firstquestion==41 :
           hintq2=1
           lb5.configure(text="此物泡過是沒有味道的 野生的會有香味且帶一點腥味")
       elif firstquestion==42 :
           hintq2=1
           lb5.configure(text="可以做成涼拌菜")
       elif firstquestion==43 :
           hintq2=1
           lb5.configure(text="此物成熟時1到1.8米高")
       elif firstquestion==44 :
           hintq2=1
           lb5.configure(text="跟大王麻辣乾麵有關的")
       elif firstquestion==45 :
           hintq2=1
           lb5.configure(text="英文叫做:carrot")
       elif firstquestion==46 :
           hintq2=1
           lb5.configure(text="此物又名:紅根菜 飛龍菜 鸚鵡菜")
       elif firstquestion==47 :
           hintq2=1
           lb5.configure(text="Subway蔬菜類有的其中一樣")
       elif firstquestion==48 :
           hintq2=1
           lb5.configure(text="楊貴妃愛吃的")
       elif firstquestion==49 :
           hintq2=1
           lb5.configure(text="跟數學符號 ∑ 有關")
       elif firstquestion==50 :
           hintq2=1
           lb5.configure(text="此字基本意思為臺階 同「的」")
       elif firstquestion==51 :
           hintq2=1
           lb5.configure(text="字的左邊為 人 部首 ")
       elif firstquestion==52 :
           hintq2=1
           lb5.configure(text="小的另外一面")
       elif firstquestion==53 :
           hintq2=1
           lb5.configure(text="英文take")
       elif firstquestion==54 :
           hintq2=1
           lb5.configure(text="許多的人")
       elif firstquestion==55 :
           hintq2=1
           lb5.configure(text="很多人不愛吃菜 因為愛吃...?")
       elif firstquestion==56 :
           hintq2=1
           lb5.configure(text="此字之意:從兩邊用力擠住")
       elif firstquestion==57 :
           hintq2=1
           lb5.configure(text="此字上面拿掉是士")
       elif firstquestion==58 :
           hintq2=1
           lb5.configure(text="X不虛傳")
       elif firstquestion==59 :
           hintq2=1
           lb5.configure(text="此字有連接之意")
       elif firstquestion==60 :
           hintq2=1
           lb5.configure(text="英文諧音Na")
       elif firstquestion==61 :
           hintq2=1
           lb5.configure(text="遇到喜歡的人會突然很緊張的地方")
       elif firstquestion==62 :
           hintq2=1
           lb5.configure(text="此字左邊 心 部首")
       elif firstquestion==63 :
           hintq2=1
           lb5.configure(text="言X信，行X果")
       elif firstquestion==64 :
           hintq2=1
           lb5.configure(text="賴加一個心")
       elif firstquestion==65 :
           hintq2=1
           lb5.configure(text="左邊為米")
       elif firstquestion==66 :
           hintq2=1
           lb5.configure(text="英文諧音Ming")
       elif firstquestion==67 :
           hintq2=1
           lb5.configure(text="筆畫十筆")
       elif firstquestion==68 :
           hintq2=1
           lb5.configure(text="此字意思有高高在上之意")
       elif firstquestion==69 :
           hintq2=1
           lb5.configure(text="中間一個十")
       elif firstquestion==70 :
           hintq2=1
           lb5.configure(text="此字拼音jiù")
       elif firstquestion==71 :
           hintq2=1
           lb5.configure(text="此字水部")
       elif firstquestion==72 :
           hintq2=1
           lb5.configure(text="此字拼音zhòng")
       elif firstquestion==73 :
           hintq2=1
           lb5.configure(text="此字有為汲水而挖掘的深洞之意")
       elif firstquestion==74 :
           hintq2=1
           lb5.configure(text="染缸裡待久了就變黑的")
       elif firstquestion==75 :
           hintq2=1
           lb5.configure(text="教授學問 知識的人")
       elif firstquestion==76 :
           hintq2=1
           lb5.configure(text="此字拼音rǎn")
       elif firstquestion==77 :
           hintq2=1
           lb5.configure(text="醜的另外一面")
       elif firstquestion==78 :
           hintq2=1
           lb5.configure(text="積少成X")
       elif firstquestion==79 :
           hintq2=1
           lb5.configure(text="此字拼音wèi")
       elif firstquestion==80 :
           hintq2=1
           lb5.configure(text="皇帝")
       elif firstquestion==81 :
           hintq2=1
           lb5.configure(text="雙位數的領頭者")
       elif firstquestion==82 :
           hintq2=1
           lb5.configure(text="比五還大的正整數")
       elif firstquestion==83 :
           hintq2=1
           lb5.configure(text="由左至右去想看看")
       elif firstquestion==84 :
           hintq2=1
           lb5.configure(text="個位數最大的字")
       elif firstquestion==85 :
           hintq2=1
           lb5.configure(text="此字可以用在某個成語當成多方面的意思")
       elif firstquestion==86 :
           hintq2=1
           lb5.configure(text="不好的字的諧音")
       elif firstquestion==87 :
           hintq2=1
           lb5.configure(text="以%率來說是滿的意思")
       elif firstquestion==88 :
           hintq2=1
           lb5.configure(text="棍子跟球各自代表什麼數字")
       elif firstquestion==89 :
           hintq2=1
           lb5.configure(text="勢均力敵的數字")
       elif firstquestion==90 :
           hintq2=1
           lb5.configure(text="考試都要當最棒的")
       elif firstquestion==91 :
           hintq2=1
           lb5.configure(text="天秤座的概念")
       elif firstquestion==92 :
           hintq2=1
           lb5.configure(text="常見為雙輪型態，但也有三輪甚至單輪")
       elif firstquestion==93 :
           hintq2=1
           lb5.configure(text="過到明年一月一號就要換的家庭物品")
       elif firstquestion==94 :
           hintq2=1
           lb5.configure(text="有不輕言倒下站著住腳的意思")
       elif firstquestion==95 :
           hintq2=1
           lb5.configure(text="太陽太大想要遮一下")
       elif firstquestion==96 :
           hintq2=1
           lb5.configure(text="與下身有關")
       elif firstquestion==97 :
           hintq2=1
           lb5.configure(text="圓柱形")
       elif firstquestion==98 :
           hintq2=1
           lb5.configure(text="可保溫")
       elif firstquestion==99 :
           hintq2=1
           lb5.configure(text="黑色的")
       elif firstquestion==100 :
           hintq2=1
           lb5.configure(text="是一個工具，跟吃的有關")
       elif firstquestion==101 :
           hintq2=1
           lb5.configure(text="投擲物")
       elif firstquestion==102 :
           hintq2=1
           lb5.configure(text="元宵節")
       elif firstquestion==103 :
           hintq2=1
           lb5.configure(text="需點燃物")
       elif firstquestion==104 :
           hintq2=1
           lb5.configure(text="與樂器有關")
       elif firstquestion==105 :
           hintq2=1
           lb5.configure(text="由上至下")
       elif firstquestion==106 :
           hintq2=1
           lb5.configure(text="也可用農村收割莊稼的器具")
       elif firstquestion==107 :
           hintq2=1
           lb5.configure(text="燃火器之一")
       elif firstquestion==108 :
           hintq2=1
           lb5.configure(text="每個學生必帶物")
       elif firstquestion==109 :
           hintq2=1
           lb5.configure(text="可張開可收起來")
       elif firstquestion==110 :
           hintq2=1
           lb5.configure(text="在台灣又稱為孔明車")
       elif firstquestion==111 :
           hintq2=1
           lb5.configure(text="野外露營必備物")
       elif firstquestion==112 :
           hintq2=1
           lb5.configure(text="是長方體")
       elif firstquestion==113 :
           hintq2=1
           lb5.configure(text="也可貼反光貼片")
       elif firstquestion==114 :
           hintq2=1
           lb5.configure(text="年輕人潮流物之一")    

def p() :
    global labels,colors
    plt.close() #一開始進入run時第一行都是先關閉原本的圖表，之後再接著用新圖表顯示
    sizes=[21.0,21.0,28.0,9.0,21.0]
    labels=["幽默冷笑話類","食物和水果類","文學造詣類","猜數字類","物品跟用品及工具類"] #labels為陣列,各題目類型的陣列
    colors=["red","green","blue","orange","pink"] #colors為陣列各題目類型顏色的陣列
    plt.pie(sizes,colors=colors,labels=labels,labeldistance=0.6,autopct="%2.0f%%",pctdistance=0.3,shadow=True,startangle=30)
    #因為進來第一行都會先run到plt.close()，所以都會把之前原本的圖表關閉掉，導致這pie沒辦法感覺到有圖表，並且感覺到有圖表那就丟的呈現，所以這裡遇到針對圖表外表的
    #圖表狀態做改變的圖形圖指令，沒有的話他就會在這裡生成第一張圖表出來，也可以說是關閉後的第一張圖表，這講法也OK，然後pie丟過去上述所說的生成的圖表之後從下行開始
    #遇到相同類型的圖形圖指令就不用像上述pie這樣子搞，直接偵測看有沒有圖表，並且偵測到看目前使用(<-重心)圖表是誰就丟過去，讓他圖表狀態改變，進而影響他圖表的外觀。
   # plt.legend()
    plt.show()

def s11() :
    global count1 #宣告函數，把外來不是跟tkinter有關相關指令用做區域變數
    count1=list1eny1.get() #count1取後方entry空白欄位(list1eny1)裡的字串值，用get()函數指令取出來
    if count1=="1" :
        list1lb2.configure(text="1") #針對list1lb2做更改指令，把text="1"丟到更改指令，然後變成針對lisrt1lb2做更改指令裡的text參數為1
        lbs1.configure(text="1.鯊魚吃了綠豆(猜食物)➠綠豆沙") #亂數設定為1
        lbs2.configure(text="2.醬油的哥哥是誰？➠醬油膏(台語諧音：豆油哥)") #亂數設定為2
        lbs3.configure(text="3.黑頭髮有什麼好處？➠不怕曬黑") #亂數設定為3
        lbs4.configure(text="4.一口井、一杯茶、兩個杯子(猜職業)➠警察伯伯 (井茶杯杯)") #亂數設定為4
        lbs5.configure(text="5.當醫生說你的病沒希望時，該怎麼辦？➠換一個醫生") #亂數設定為5
        lbs6.configure(text="6.小孩子跌倒(猜成語)➠馬馬虎虎(媽媽撫撫)") #亂數設定為6
        lbs7.configure(text="7.什麼車最多燈？➠垃圾車(因為它會一邊放音樂：燈燈燈燈燈燈燈~)") #亂數設定為7
        lbs8.configure(text="8.請問iPhone在哪個大學最難用？➠南華科技大學(難滑科技大學)") #亂數設定為8
    elif count1=="2" :
        list1lb2.configure(text="2") #針對list1lb2做更改指令，把text="2"丟到更改指令，然後變成針對lisrt1lb2做更改text參數為2指令
        lbs1.configure(text="9.「3」在路上走呀走，翻了兩次跟斗(猜成語)➠三番兩次") #亂數設定為9
        lbs2.configure(text="10.4個人在屋子打麻將，警察來了為什麼帶走5個人？➠因為他們打的人叫麻將") #亂數設定為10
        lbs3.configure(text="11.Costco鬧鬼(猜成語)➠好事多磨(好市多魔)") #亂數設定為11
        lbs4.configure(text="12.Hello Kitty賣光光(猜台灣地名)➠貓空") #亂數設定為12
        lbs5.configure(text="13.ㄊㄞˊ(猜一個古代人名)➠祝英台(注音台)") #亂數設定為13
        lbs6.configure(text="14.他走了的英文怎麼說？➠IKEA(台語諧音)") #亂數設定為14
        lbs7.configure(text="15.冬瓜、西瓜、南瓜都能吃，什麼瓜不能吃？➠傻瓜") #亂數設定為15
        lbs8.configure(text="16.只騙中年人(猜成語)➠童叟無欺") #亂數設定為16
    elif count1=="3" :
        list1lb2.configure(text="3") #針對list1lb2做更改指令，把text="3"丟到更改指令，然後變成針對lisrt1lb2做更改指令裡的text參數為3
        lbs1.configure(text="17.打什麼東西，不必花力氣？➠打瞌睡") #亂數設定為17
        lbs2.configure(text="18.玉米燙頭髮變成什麼(猜食物)➠爆米花") #亂數設定為18
        lbs3.configure(text="19.一塊錢可以買幾頭牛？➠九十頭 (因為九牛一毛)") #亂數設定為19
        lbs4.configure(text="20.真正的豬喝什麼飲料？➠珍珠奶茶") #亂數設定為20
        lbs5.configure(text="21.真實的山，冒充的海(猜成語)➠山珍海味") #亂數設定為21
        lbs6.configure(text="22.一頭豬說：加油！(猜食物)➠朱古力") #亂數設定為22
        lbs7.configure(text="23.馬克，約翰，湯姆，誰可以讓比薩斜塔不倒下來？➠約翰(因為約翰去扶塔/約翰屈伏塔)") #亂數設定為23
        lbs8.configure(text="24.被人家放了鴿子還很高興的是誰？➠鴿子") #亂數設定為24

def s21() :
    global count2 #宣告函數，把外來不是跟tkinter有關相關指令用做區域變數
    count2=list2eny1.get()
    if count2=="1" :
        list2lb2.configure(text="1")
        lbss1.configure(text="1.一個婆婆園中站，身上掛滿小雞蛋，又有紅來又有綠，既好吃來又好看(猜食物)➠棗樹") #亂數設定為25
        lbss2.configure(text="2.小刺蝟，毛外套，脫了外套露紫袍，袍裏套着紅絨襖，襖裏睡個小寶寶(猜食物)➠栗子") #亂數設定為26
        lbss3.configure(text="3.不是蔥不是蒜，一層一層裹紫緞，說蔥比蔥長得矮，像蒜就是不分瓣(猜蔬菜)➠洋蔥") #亂數設定為27
        lbss4.configure(text="4.兄弟七八個，圍着柱子坐，大家一分家，衣服就扯破(猜蔬菜)➠蒜") #亂數設定為28
        lbss5.configure(text="5.白白一片似雪花，落下水裏不見(猜食物)➠鹽") #亂數設定為29
        lbss6.configure(text="6.白牀鋪，黃帳子(猜食物)➠桂圓") #亂數設定為30
        lbss7.configure(text="7.白胖娃娃泥裏臥，腰身細細心眼多(猜食物)➠藕") #亂數設定為31
        lbss8.configure(text="8.白胖胖，四方方，一塊一塊擺桌上，能做菜，能做湯，常常吃它有營養(猜食物)➠豆腐") #亂數設定為32
    elif count2=="2" :
        list2lb2.configure(text="2") 
        lbss1.configure(text="9.白糖梅子真稀奇(猜食物)➠元宵") #亂數設定為33
        lbss2.configure(text="10.百姐妹，千姐妹，同床睡，各蓋被(猜水果)➠石榴") #亂數設定為34
        lbss3.configure(text="11.把把綠傘土裏插，條條紫藤地上爬，地上長葉不開花，地下結串大甜瓜(猜食物)➠紅薯") #亂數設定為35
        lbss4.configure(text="12.身子長，個不大，遍體長着小疙瘩，有人見了皺眉頭，有人見了樂開花(猜蔬菜)➠苦瓜") #亂數設定為36
        lbss5.configure(text="13.身材瘦瘦個兒高，葉兒細細披綠袍，別看樣子像青蒿，香氣撲鼻味兒好(猜蔬菜)➠芹菜") #亂數設定為37
        lbss6.configure(text="14.身體圓圓沒有毛，不是桔子不是桃，雲裏霧裏過幾夜，脫去綠衣換紅袍(猜水果)➠柿子") #亂數設定為38
        lbss7.configure(text="15.來自水中，卻怕水衝，回到水裏，無影無蹤(猜食物)➠鹽") #亂數設定為39
        lbss8.configure(text="16.味道甜甜營養多，誰說無花只結果，其實花開密又小，切莫被名所迷惑(猜食物)➠無花果") #亂數設定為40
    elif count2=="3" :
        list2lb2.configure(text="3")
        lbss1.configure(text="17.狀如蘑菇一珍寶，當年白蛇將它盜，其實是味好草藥，滋補健身價值高(猜食物)➠靈芝") #亂數設定為41
        lbss2.configure(text="18.青皮包白肉，像個大枕頭，莫聽名字冷，熱天菜場有(猜蔬菜)➠冬瓜") #亂數設定為42
        lbss3.configure(text="19.春穿綠衣秋黃袍，頭兒彎彎垂珠寶，從幼到老難離水，不洗澡來只泡腳(猜食物)➠水稻") #亂數設定為43
        lbss4.configure(text="20.紅口袋，綠口袋，有人怕，有人愛，愛它是樣好小菜，怕它吃到嘴裏眼淚來(猜蔬菜)➠辣椒") #亂數設定為44
        lbss5.configure(text="21.紅公雞，綠公雞，身子鑽在泥底下，你要捉住它，揪住尾巴用力拔(猜蔬菜)➠胡蘿蔔") #亂數設定為45
        lbss6.configure(text="22.紅嘴綠鸚哥，吃了營養多(猜蔬菜)➠菠菜") #亂數設定為46
        lbss7.configure(text="23.個兒小小，頭尾尖尖，初嘗皺眉，再吃開顏(猜食物)➠橄欖") #亂數設定為47
        lbss8.configure(text="24.脫了紅袍子，是個白胖子，去了白胖子，剩個黑丸子(猜水果)➠荔枝") #亂數設定為48

def s31() :
    global count3
    count3=list3eny1.get()
    if count3=="1" :
        list3lb2.configure(text="1")
        lbsss1.configure(text="1.2+6(猜一字)➠積") #亂數設定為49
        lbsss2.configure(text="2.242÷22(猜一字)➠墑") #亂數設定為50
        lbsss3.configure(text="3.4個人搬個木頭(猜一字)➠傑") #亂數設定為51
        lbsss4.configure(text="4.一人(猜一字)➠大") #亂數設定為52
        lbsss5.configure(text="5.一人一張口，下面長隻手(猜一字)➠拿") #亂數設定為53
        lbsss6.configure(text="6.一人比兩人高(猜一字)➠眾") #亂數設定為54
        lbsss7.configure(text="7.一人在內(猜一字)➠肉") #亂數設定為55
        lbsss8.configure(text="8.一人挑兩小人(猜一字)➠夾") #亂數設定為56
    elif count3=="2" :
        list3lb2.configure(text="2")
        lbsss1.configure(text="9.一口吃掉牛尾巴(猜一字)➠告") #亂數設定為57
        lbsss2.configure(text="10.一口咬去多半截(猜一字)➠名") #亂數設定為58
        lbsss3.configure(text="11.一口咬定(猜一字)➠交") #亂數設定為59
        lbsss4.configure(text="12.一大二小(猜一字)➠奈") #亂數設定為60
        lbsss5.configure(text="13.一勾心月伴三星(猜一字)➠心") #亂數設定為61
        lbsss6.configure(text="14.一心一意(猜一字)➠憶") #亂數設定為62
        lbsss7.configure(text="15.一心向上(猜一字)➠必") #亂數設定為63
        lbsss8.configure(text="16.一心依賴實為惰(猜一字)➠懶") #亂數設定為64
    elif count3=="3" :
        list3lb2.configure(text="3")
        lbsss1.configure(text="17.一斗米(猜一字)➠料") #亂數設定為65
        lbsss2.configure(text="18.一月一日非今天(猜一字)➠明") #亂數設定為66
        lbsss3.configure(text="19.一月七日(猜一字)➠脂") #亂數設定為67
        lbsss4.configure(text="20.一加一(猜一字)➠王") #亂數設定為68
        lbsss5.configure(text="21.一加一不是二(猜一字)➠王") #亂數設定為69
        lbsss6.configure(text="22.一半兒(猜一字)➠臼") #亂數設定為70
        lbsss7.configure(text="23.一字十三點，難在如何點(猜一字)➠汁") #亂數設定為71
        lbsss8.configure(text="24.一字六筆無豎橫，同心同德力無窮(猜一字)➠眾") #亂數設定為72
    elif count3=="4" :
        list3lb2.configure(text="4")
        lbsss1.configure(text="25.一字生得巧，四面八隻腳(猜一字)➠井") #亂數設定為73
        lbsss2.configure(text="26.一百減一(猜一字)➠白") #亂數設定為74
        lbsss3.configure(text="27.一走就帶千軍(猜一字)➠師") #亂數設定為75
        lbsss4.configure(text="28.一來再來(猜一字)➠冉") #亂數設定為76
        lbsss5.configure(text="29.一來就有徒弟(猜一字)➠帥") #亂數設定為77
        lbsss6.configure(text="30.一夜又一夜(猜一字)➠多") #亂數設定為78
        lbsss7.configure(text="31.一柱擎天(猜一字)➠未") #亂數設定為79
        lbsss8.configure(text="32.一流水準(猜一字)➠淮") #亂數設定為80

def s41() :
    global count4
    count4=list4eny1.get()
    if count4=="1" :
        list4lb2.configure(text="1")
        lbssss1.configure(text="1.一來就千(猜數字國字)➠十") #亂數設定為81
        lbssss2.configure(text="2.八個螞蟻擡棍棍，一個螞蟻棍上昆(猜數字國字)➠六") #亂數設定為82
        lbssss3.configure(text="3.三與三，嘴對嘴(猜數字)➠8") #亂數設定為83
        lbssss4.configure(text="4.旭日東昇(猜數字國字)➠九") #亂數設定為84
        lbssss5.configure(text="5.兩隻鳥兒對頭飛，一隻瘦來一隻肥(猜數字國字)➠八") #亂數設定為85
        lbssss6.configure(text="6.除了2還是2(猜數字)➠4") #亂數設定為86
        lbssss7.configure(text="7.添一筆，增百倍，減一筆，少九成(猜數字國字)➠十") #亂數設定為87
        lbssss8.configure(text="8.棍子打棒球(猜數字)➠10") #亂數設定為88
    elif count4=="2" :
        list4lb2.configure(text="2")
        lbssss1.configure(text="9.語言不通難開口(猜數字國字)➠五") #亂數設定為89
        lbssss2.configure(text="10.數字雖小，卻在百萬之上(猜數字國字)➠一") #亂數設定為90
        lbssss3.configure(text="")
        lbssss4.configure(text="")
        lbssss5.configure(text="")
        lbssss6.configure(text="")
        lbssss7.configure(text="")
        lbssss8.configure(text="")

def s51() :
    global count5
    count5=list5eny1.get()
    if count5=="1" :
        list5lb2.configure(text="1")
        lbsssss1.configure(text="1.一匹馬兒兩人騎，這邊高來那邊低， 雖然馬兒不會跑，兩人騎着笑嘻嘻(猜一物)➠蹺蹺板") #亂數設定為91
        lbsssss2.configure(text="2.一匹馬兒真正好，沒有尾巴沒有腳，不喝水來不吃草，騎上它就滿街跑唱(猜一物)➠自行車") #亂數設定為92
        lbsssss3.configure(text="3.一天過去，脫件衣裳，一年過去，全身脫光(猜一物)➠日曆") #亂數設定為93
        lbsssss4.configure(text="4.一位公公精神好，從小到老不睡覺。身體輕，勁不小，左推右推推不倒(猜一物)➠不倒翁") #亂數設定為94
        lbsssss5.configure(text="5.一物生得巧，地位比人高。戴上御風寒，脫下有禮貌(猜一物)➠帽子") #亂數設定為95
        lbsssss6.configure(text="6.一物參個口，你有我也有，有他不怎樣，無他就現醜(猜一物)➠褲子") #亂數設定為96
        lbsssss7.configure(text="7.一個大肚皮，生來怪脾氣， 不打不做聲，越打越歡喜(猜一物)➠鼓") #亂數設定為97
        lbsssss8.configure(text="8.一個小兒郎，每天站桌上。肚裏滾滾熱，肚皮冰冰涼。一個大耳朵，穿件花衣裳(猜一物)➠暖水瓶") #亂數設定為98
    elif count5=="2" :
        list5lb2.configure(text="2")
        lbsssss1.configure(text="9.一個小黑人，跳進洗澡盆，越洗越不凈，長人變短人(猜一物)➠墨") #亂數設定為99
        lbsssss2.configure(text="10.一個小碗尾巴長，能盛飯菜能盛湯。盛上又倒了，倒了再盛上(猜一物)➠小勺") #亂數設定為100
        lbsssss3.configure(text="11.一個瓜，腰上掛，抽了筋，就開花，消滅敵人要用它(猜一物)➠手榴彈") #亂數設定為101
        lbsssss4.configure(text="12.一個南瓜兩頭兒空，肚裏開花放光明，有瓜沒葉兒高高掛，照得面前一片紅(猜一物)➠燈籠") #亂數設定為102
        lbsssss5.configure(text="13.一個娃娃小不點，一件紅襖身上穿，香火把它的辮子點，大叫一聲飛上天(猜一物)➠爆竹") #亂數設定為103
        lbsssss6.configure(text="14.一個風箱真奇怪，一拉它就唱起來(猜一物)➠手風琴") #亂數設定為104
        lbsssss7.configure(text="15.一座橋，地上架，走着上去坐着下(猜一物)➠滑梯") #亂數設定為105
        lbsssss8.configure(text="16.一根小木棒，安個彎月亮。秋天收莊稼，請它來幫忙唱(猜一物)➠鐮刀") #亂數設定為106
    elif count5=="3" :
        list5lb2.configure(text="3")
        lbsssss1.configure(text="17.一根小棍兒，頂個圓粒兒， 小孩兒玩它，容易出事兒(猜一物)➠火柴") #亂數設定為107
        lbsssss2.configure(text="18.一根竹管二尺長，開了七個小圓窗， 對準一個小窗口，吹陣風就把歌唱(猜一物)➠笛子") #亂數設定為108
        lbsssss3.configure(text="19.一根柱子好些樑，沒有門窗沒有牆，好象一座小亭子，用它擋雨遮太陽(猜一物)➠傘") #亂數設定為109
        lbsssss4.configure(text="20.一條怪牛，兩條圓腿，騎他肚上，抓他雙角(猜一物)➠自行車") #亂數設定為110
        lbsssss5.configure(text="21.一間小藥房，藥品裡面藏。房子塗白色，十字畫中央(猜一物)➠醫藥箱") #亂數設定為111
        lbsssss6.configure(text="22.一間房子扁又長，上邊開了許多窗，用嘴吹進一陣風，好聽的音樂多響亮(猜一物)➠口琴") #亂數設定為112
        lbsssss7.configure(text="23.一樣東西亮晶晶，又光又硬又透明，工人叔叔造出來，它的用處數不清(猜一物)➠玻璃") #亂數設定為113
        lbsssss8.configure(text="24.一雙玉燕靠地飛，早上出門夜裏歸(猜一物)➠鞋子") #亂數設定為114

def introductions() :
    introdw=s.Tk()
    introdw.title("規則介紹")
    introdw.geometry("350x300")
    introdlb1=s.Label(introdw,text="本遊戲可單人挑戰或雙人挑戰(建議2人)")
    introdlb2=s.Label(introdw,text="單人挑戰:可以挑戰自己自身分數!")
    introdlb3=s.Label(introdw,text="雙人挑戰:可以雙方各自定好要PK幾題，然後一題設置答題")
    introdlb4=s.Label(introdw,text="                 時間，並且依照各自分數高低判斷勝負!")
    introdlb5=s.Label(introdw,text="開始/下一題按鈕是代表開始及接著要下一題。")
    introdlb6=s.Label(introdw,text="提示1跟提示2按鈕代表每題有兩個提示，答對後發現每用一")
    introdlb7=s.Label(introdw,text="個提示就會獲得的答對分數-1，全用就-2，都沒用然後答對")
    introdlb8=s.Label(introdw,text="就+3分。")
    introdlb9=s.Label(introdw,text="結束這一輪的挑戰就按下清除按鈕，就會全部清掉重新。")
    introdlb1.place(x=10,y=10)
    introdlb2.place(x=20,y=45)
    introdlb3.place(x=20,y=70)
    introdlb4.place(x=20,y=95)
    introdlb5.place(x=10,y=140)
    introdlb6.place(x=10,y=160)
    introdlb7.place(x=10,y=180)
    introdlb8.place(x=10,y=200)
    introdlb9.place(x=10,y=230)
    introdw.mainloop()

def suretosure() :
    global hintq1,hintq2,user,imok
    if start==1 : #如果目前start等於1,代表還在這一輪的猜燈謎
        if firstquestion==1 and imok==1 : #進來後如果是抽到第一題和(and)imok機關代表答題機會沒用掉就進去
            if eny1.get()=="綠豆沙" : #如果你的答案是綠豆沙進入
                if hintq1==0 and hintq2==0 : #提示1和提示2都為0,代表雙方都沒用提示,就進去
                    imok=0 #答題機關用0,防止有心人士刷分,所以只能等下一次的開始/下一題按鈕歸為1了,也就是重抽題目歸為1了
                    answerr.configure(text="A: 綠豆沙") #answerr用configure更改指令用意原理,把answerr的text改成題目答案
                    user+=3 #答對總分數+3
                    scores.configure(text=""+str(user)) #scores用configure更改指令用意原理,把scores的text改成當前答對總分數
                    hintq1=0 #提示1歸0,給抽到的下一題使用
                    hintq2=0 #提示2歸0,給抽到的下一題使用
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 綠豆沙")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 綠豆沙")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else : #來到else這代表你答案不是輸入綠豆沙,所以錯誤
                answerr.configure(text="A: 綠豆沙") #answerr用configure更改指令用意原理,把answerr的text改成當前該題的題目答案出來公佈
                imok=0 #答案機關用0,防止有心人士刷分,怕改成題目答案後在按一次+分,所以只能等下一次的開始/下一題按鈕歸為1了,也就是重抽題目歸為1了
        elif firstquestion==2 and imok==1 :
            if eny1.get()=="醬油膏" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 醬油膏(台語諧音:豆油哥)")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 醬油膏(台語諧音:豆油哥)")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 醬油膏(台語諧音:豆油哥)")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 醬油膏(台語諧音:豆油哥)")
                imok=0
        elif firstquestion==3 and imok==1 :
            if eny1.get()=="不怕曬黑" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 不怕曬黑")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 不怕曬黑")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 不怕曬黑")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 不怕曬黑")
                imok=0
        elif firstquestion==4 and imok==1 :
            if eny1.get()=="警察伯伯" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 警察伯伯 (井茶杯杯)")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 警察伯伯 (井茶杯杯)")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 警察伯伯 (井茶杯杯)")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 警察伯伯 (井茶杯杯)")
                imok=0
        elif firstquestion==5 and imok==1 :
            if eny1.get()=="換一個醫生" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 換一個醫生")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 換一個醫生")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 換一個醫生")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 換一個醫生")
                imok=0
        elif firstquestion==6 and imok==1 :
            if eny1.get()=="馬馬虎虎" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 馬馬虎虎(媽媽撫撫)")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 馬馬虎虎(媽媽撫撫)")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 馬馬虎虎(媽媽撫撫)")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 馬馬虎虎(媽媽撫撫)")
                imok=0
        elif firstquestion==7 and imok==1 :
            if eny1.get()=="垃圾車" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 垃圾車(因為它會一邊放音樂：燈燈燈燈燈燈燈~)")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 垃圾車(因為它會一邊放音樂：燈燈燈燈燈燈燈~)")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 垃圾車(因為它會一邊放音樂：燈燈燈燈燈燈燈~)")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 垃圾車(因為它會一邊放音樂：燈燈燈燈燈燈燈~)")
                imok=0
        elif firstquestion==8 and imok==1 :
            if eny1.get()=="南華科技大學" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 南華科技大學(難滑科技大學)")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 南華科技大學(難滑科技大學)")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 南華科技大學(難滑科技大學)")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 南華科技大學(難滑科技大學)")
                imok=0
        elif firstquestion==9 and imok==1 :
            if eny1.get()=="三番兩次" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 三番兩次")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 三番兩次")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 三番兩次")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 三番兩次")
                imok=0
        elif firstquestion==10 and imok==1 :
            if eny1.get()=="因為他們打的人叫麻將" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 因為他們打的人叫麻將")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 因為他們打的人叫麻將")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 因為他們打的人叫麻將")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 因為他們打的人叫麻將")
                imok=0        
        elif firstquestion==11 and imok==1 :
            if eny1.get()=="好事多磨" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 好事多磨(好市多魔)")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 好事多磨(好市多魔)")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 好事多磨(好市多魔)")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 好事多磨(好市多魔)")
                imok=0
        elif firstquestion==12 and imok==1 :
            if eny1.get()=="貓空" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 貓空")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 貓空")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 貓空")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 貓空")
                imok=0
        elif firstquestion==13 and imok==1 :
            if eny1.get()=="祝英台" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 祝英台(注音台)")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 祝英台(注音台)")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 祝英台(注音台)")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 祝英台(注音台)")
                imok=0
        elif firstquestion==14 and imok==1 :
            if eny1.get()=="IKEA" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: IKEA(台語諧音)")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: IKEA(台語諧音)")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: IKEA(台語諧音)")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: IKEA(台語諧音)")
                imok=0
        elif firstquestion==15 and imok==1 :
            if eny1.get()=="傻瓜" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 傻瓜")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 傻瓜")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 傻瓜")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 傻瓜")
                imok=0
        elif firstquestion==16 and imok==1 :
            if eny1.get()=="童叟無欺" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 童叟無欺")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 童叟無欺")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 童叟無欺")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 童叟無欺")
                imok=0
        elif firstquestion==17 and imok==1 :
            if eny1.get()=="打瞌睡" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 打瞌睡")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 打瞌睡")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 打瞌睡")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 打瞌睡")
                imok=0 
        elif firstquestion==18 and imok==1 :
            if eny1.get()=="爆米花" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 爆米花")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 爆米花")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 爆米花")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 爆米花")
                imok=0
        elif firstquestion==19 and imok==1 :
            if eny1.get()=="九十頭" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 九十頭 (因為九牛一毛)")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 九十頭 (因為九牛一毛)")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 九十頭 (因為九牛一毛)")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 九十頭 (因為九牛一毛)")
                imok=0
        elif firstquestion==20 and imok==1 :
            if eny1.get()=="珍珠奶茶" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 珍珠奶茶")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 珍珠奶茶")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 珍珠奶茶")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 珍珠奶茶")
                imok=0
        elif firstquestion==21 and imok==1 :
            if eny1.get()=="山珍海味" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 山珍海味")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 山珍海味")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 山珍海味")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 山珍海味")
                imok=0
        elif firstquestion==22 and imok==1 :
            if eny1.get()=="朱古力" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 朱古力")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 朱古力")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 朱古力")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 朱古力")
                imok=0
        elif firstquestion==23 and imok==1 :
            if eny1.get()=="約翰" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 約翰(因為約翰去扶塔/約翰屈伏塔)")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 約翰(因為約翰去扶塔/約翰屈伏塔)")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 約翰(因為約翰去扶塔/約翰屈伏塔)")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 約翰(因為約翰去扶塔/約翰屈伏塔)")
                imok=0
        elif firstquestion==24 and imok==1 :
            if eny1.get()=="鴿子" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 鴿子")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 鴿子")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 鴿子")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 鴿子")
                imok=0
        elif firstquestion==25 and imok==1 :
            if eny1.get()=="棗樹" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 棗樹")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 棗樹")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 棗樹")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 棗樹")
                imok=0
        elif firstquestion==26 and imok==1 :
            if eny1.get()=="栗子" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 栗子")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 栗子")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 栗子")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 栗子")
                imok=0
        elif firstquestion==27 and imok==1 :
            if eny1.get()=="洋蔥" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 洋蔥")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 洋蔥")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 洋蔥")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 洋蔥")
                imok=0
        elif firstquestion==28 and imok==1 :
            if eny1.get()=="蒜" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 蒜")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 蒜")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 蒜")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 蒜")
                imok=0 
        elif firstquestion==29 and imok==1 :
            if eny1.get()=="鹽" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 鹽")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 鹽")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 鹽")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 鹽")
                imok=0
        elif firstquestion==30 and imok==1 :
            if eny1.get()=="桂圓" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 桂圓")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 桂圓")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 桂圓")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 桂圓")
                imok=0 
        elif firstquestion==31 and imok==1 :
            if eny1.get()=="藕" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 藕")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 藕")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 藕")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 藕")
                imok=0 
        elif firstquestion==32 and imok==1 :
            if eny1.get()=="豆腐" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 豆腐")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 豆腐")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 豆腐")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 豆腐")
                imok=0
        elif firstquestion==33 and imok==1 :
            if eny1.get()=="元宵" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 元宵")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 元宵")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 元宵")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 元宵")
                imok=0
        elif firstquestion==34 and imok==1 :
            if eny1.get()=="石榴" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 石榴")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 石榴")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 石榴")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 石榴")
                imok=0
        elif firstquestion==35 and imok==1 :
            if eny1.get()=="紅薯" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 紅薯")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 紅薯")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 紅薯")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 紅薯")
                imok=0
        elif firstquestion==36 and imok==1 :
            if eny1.get()=="苦瓜" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 苦瓜")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 苦瓜")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 苦瓜")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 苦瓜")
                imok=0
        elif firstquestion==37 and imok==1 :
            if eny1.get()=="芹菜" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 芹菜")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 芹菜")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 芹菜")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 芹菜")
                imok=0
        elif firstquestion==38 and imok==1 :
            if eny1.get()=="柿子" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 柿子")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 柿子")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 柿子")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 柿子")
                imok=0
        elif firstquestion==39 and imok==1 :
            if eny1.get()=="鹽" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 鹽")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 鹽")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 鹽")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 鹽")
                imok=0
        elif firstquestion==40 and imok==1 :
            if eny1.get()=="無花果" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 無花果")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 無花果")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 無花果")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 無花果")
                imok=0
        elif firstquestion==41 and imok==1 :
            if eny1.get()=="靈芝" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 靈芝")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 靈芝")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 靈芝")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 靈芝")
                imok=0
        elif firstquestion==42 and imok==1 :
            if eny1.get()=="冬瓜" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 冬瓜")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 冬瓜")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 冬瓜")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 冬瓜")
                imok=0
        elif firstquestion==43 and imok==1 :
            if eny1.get()=="水稻" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 水稻")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 水稻")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 水稻")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 水稻")
                imok=0
        elif firstquestion==44 and imok==1 :
            if eny1.get()=="辣椒" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 辣椒")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 辣椒")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 辣椒")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 辣椒")
                imok=0
        elif firstquestion==45 and imok==1 :
            if eny1.get()=="胡蘿蔔" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 胡蘿蔔")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 胡蘿蔔")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 胡蘿蔔")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 胡蘿蔔")
                imok=0
        elif firstquestion==46 and imok==1 :
            if eny1.get()=="菠菜" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 菠菜")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 菠菜")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 菠菜")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 菠菜")
                imok=0
        elif firstquestion==47 and imok==1 :
            if eny1.get()=="橄欖" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 橄欖")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 橄欖")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 橄欖")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 橄欖")
                imok=0
        elif firstquestion==48 and imok==1 :
            if eny1.get()=="荔枝" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 荔枝")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 荔枝")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 荔枝")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 荔枝")
                imok=0
        elif firstquestion==49 and imok==1 :
            if eny1.get()=="積" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 積")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 積")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 積")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 積")
                imok=0
        elif firstquestion==50 and imok==1 :
            if eny1.get()=="墑" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 墑")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 墑")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 墑")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 墑")
                imok=0
        elif firstquestion==51 and imok==1 :
            if eny1.get()=="傑" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 傑")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 傑")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 傑")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 傑")
                imok=0
        elif firstquestion==52 and imok==1 :
            if eny1.get()=="大" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 大")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 大")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 大")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 大")
                imok=0
        elif firstquestion==53 and imok==1 :
            if eny1.get()=="拿" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 拿")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 拿")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 拿")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 拿")
                imok=0
        elif firstquestion==54 and imok==1 :
            if eny1.get()=="眾" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 眾")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 眾")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 眾")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 眾")
                imok=0
        elif firstquestion==55 and imok==1 :
            if eny1.get()=="肉" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 肉")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 肉")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 肉")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 肉")
                imok=0
        elif firstquestion==56 and imok==1 :
            if eny1.get()=="夾" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 夾")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 夾")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 夾")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 夾")
                imok=0
        elif firstquestion==57 and imok==1 :
            if eny1.get()=="告" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 告")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 告")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 告")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 告")
                imok=0
        elif firstquestion==58 and imok==1 :
            if eny1.get()=="名" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 名")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 名")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 名")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 名")
                imok=0
        elif firstquestion==59 and imok==1 :
            if eny1.get()=="交" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 交")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 交")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 交")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 交")
                imok=0
        elif firstquestion==60 and imok==1 :
            if eny1.get()=="奈" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 奈")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 奈")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 奈")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 奈")
                imok=0
        elif firstquestion==61 and imok==1 :
            if eny1.get()=="心" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 心")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 心")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 心")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 心")
                imok=0
        elif firstquestion==62 and imok==1 :
            if eny1.get()=="憶" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 憶")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 憶")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 憶")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 憶")
                imok=0
        elif firstquestion==63 and imok==1 :
            if eny1.get()=="必" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 必")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 必")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 必")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 必")
                imok=0
        elif firstquestion==64 and imok==1 :
            if eny1.get()=="懶" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 懶")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 懶")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 懶")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 懶")
                imok=0
        elif firstquestion==65 and imok==1 :
            if eny1.get()=="料" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 料")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 料")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 料")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 料")
                imok=0
        elif firstquestion==66 and imok==1 :
            if eny1.get()=="明" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 明")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 明")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 明")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 明")
                imok=0
        elif firstquestion==67 and imok==1 :
            if eny1.get()=="脂" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 脂")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 脂")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 脂")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 脂")
                imok=0
        elif firstquestion==68 and imok==1 :
            if eny1.get()=="王" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 王")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 王")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 王")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 王")
                imok=0
        elif firstquestion==69 and imok==1 :
            if eny1.get()=="王" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 王")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 王")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 王")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 王")
                imok=0
        elif firstquestion==70 and imok==1 :
            if eny1.get()=="臼" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 臼")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 臼")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 臼")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 臼")
                imok=0
        elif firstquestion==71 and imok==1 :
            if eny1.get()=="汁" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 汁")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 汁")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 汁")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 汁")
                imok=0
        elif firstquestion==72 and imok==1 :
            if eny1.get()=="眾" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 眾")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 眾")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 眾")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 眾")
                imok=0
        elif firstquestion==73 and imok==1 :
            if eny1.get()=="井" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 井")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 井")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 井")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 井")
                imok=0
        elif firstquestion==74 and imok==1 :
            if eny1.get()=="白" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 白")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 白")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 白")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 白")
                imok=0
        elif firstquestion==75 and imok==1 :
            if eny1.get()=="師" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 師")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 師")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 師")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 師")
                imok=0
        elif firstquestion==76 and imok==1 :
            if eny1.get()=="冉" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 冉")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 冉")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 冉")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 冉")
                imok=0
        elif firstquestion==77 and imok==1 :
            if eny1.get()=="帥" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 帥")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 帥")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 帥")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 帥")
                imok=0
        elif firstquestion==78 and imok==1 :
            if eny1.get()=="多" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 多")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 多")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 多")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 多")
                imok=0
        elif firstquestion==79 and imok==1 :
            if eny1.get()=="未" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 未")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 未")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 未")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 未")
                imok=0
        elif firstquestion==80 and imok==1 :
            if eny1.get()=="淮" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 淮")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 淮")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 淮")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 淮")
                imok=0
        elif firstquestion==81 and imok==1 :
            if eny1.get()=="十" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 十")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 十")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 十")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 十")
                imok=0
        elif firstquestion==82 and imok==1 :
            if eny1.get()=="六" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 六")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 六")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 六")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 六")
                imok=0
        elif firstquestion==83 and imok==1 :
            if eny1.get()=="8" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 8")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 8")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 8")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 8")
                imok=0
        elif firstquestion==84 and imok==1 :
            if eny1.get()=="九" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 九")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 九")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 九")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 九")
                imok=0
        elif firstquestion==85 and imok==1 :
            if eny1.get()=="八" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 八")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 八")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 八")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 八")
                imok=0
        elif firstquestion==86 and imok==1 :
            if eny1.get()=="4" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 4")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 4")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 4")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 4")
                imok=0
        elif firstquestion==87 and imok==1 :
            if eny1.get()=="十" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 十")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 十")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 十")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 十")
                imok=0
        elif firstquestion==88 and imok==1 :
            if eny1.get()=="10" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 10")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 10")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 10")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 10")
                imok=0
        elif firstquestion==89 and imok==1 :
            if eny1.get()=="五" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 五")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 五")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 五")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 五")
                imok=0
        elif firstquestion==90 and imok==1 :
            if eny1.get()=="一" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 一")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 一")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 一")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 一")
                imok=0
        elif firstquestion==91 and imok==1 :
            if eny1.get()=="蹺蹺板" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 蹺蹺板")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 蹺蹺板")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 蹺蹺板")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 蹺蹺板")
                imok=0
        elif firstquestion==92 and imok==1 :
            if eny1.get()=="自行車" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 自行車")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 自行車")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 自行車")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 自行車")
                imok=0
        elif firstquestion==93 and imok==1 :
            if eny1.get()=="日曆" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 日曆")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 日曆")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 日曆")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 日曆")
                imok=0
        elif firstquestion==94 and imok==1 :
            if eny1.get()=="不倒翁" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 不倒翁")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 不倒翁")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 不倒翁")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 不倒翁")
                imok=0
        elif firstquestion==95 and imok==1 :
            if eny1.get()=="帽子" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 帽子")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 帽子")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 帽子")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 不倒翁")
                imok=0
        elif firstquestion==96 and imok==1 :
            if eny1.get()=="褲子" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 褲子")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 褲子")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 褲子")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 褲子")
                imok=0
        elif firstquestion==97 and imok==1 :
            if eny1.get()=="鼓" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 鼓")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 鼓")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 鼓")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 鼓")
                imok=0
        elif firstquestion==98 and imok==1 :
            if eny1.get()=="暖水瓶" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 暖水瓶")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 暖水瓶")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 暖水瓶")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 暖水瓶")
                imok=0
        elif firstquestion==99 and imok==1 :
            if eny1.get()=="墨" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 墨")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 墨")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 墨")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 墨")
                imok=0
        elif firstquestion==100 and imok==1 :
            if eny1.get()=="小勺" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 小勺")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 小勺")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 小勺")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 小勺")
                imok=0
        elif firstquestion==101 and imok==1 :
            if eny1.get()=="手榴彈" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 手榴彈")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 手榴彈")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 手榴彈")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 手榴彈")
                imok=0
        elif firstquestion==102 and imok==1 :
            if eny1.get()=="燈籠" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 燈籠")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 燈籠")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 燈籠")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 燈籠")
                imok=0
        elif firstquestion==103 and imok==1 :
            if eny1.get()=="爆竹" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 爆竹")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 爆竹")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 爆竹")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 爆竹")
                imok=0
        elif firstquestion==104 and imok==1 :
            if eny1.get()=="手風琴" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 手風琴")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 手風琴")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 手風琴")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 手風琴")
                imok=0
        elif firstquestion==105 and imok==1 :
            if eny1.get()=="滑梯" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 滑梯")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 滑梯")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 滑梯")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 滑梯")
                imok=0
        elif firstquestion==106 and imok==1 :
            if eny1.get()=="鐮刀" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 鐮刀")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 鐮刀")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 鐮刀")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 鐮刀")
                imok=0
        elif firstquestion==107 and imok==1 :
            if eny1.get()=="火柴" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 火柴")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 火柴")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 火柴")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 火柴")
                imok=0
        elif firstquestion==108 and imok==1 :
            if eny1.get()=="笛子" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 笛子")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 笛子")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 笛子")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 笛子")
                imok=0
        elif firstquestion==109 and imok==1 :
            if eny1.get()=="傘" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 傘")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 傘")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 傘")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 傘")
                imok=0
        elif firstquestion==110 and imok==1 :
            if eny1.get()=="自行車" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 自行車")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 自行車")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 自行車")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 自行車")
                imok=0
        elif firstquestion==111 and imok==1 :
            if eny1.get()=="醫藥箱" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 醫藥箱")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 醫藥箱")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 醫藥箱")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 醫藥箱")
                imok=0
        elif firstquestion==112 and imok==1 :
            if eny1.get()=="口琴" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 口琴")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 口琴")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 口琴")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 口琴")
                imok=0
        elif firstquestion==113 and imok==1 :
            if eny1.get()=="玻璃" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 玻璃")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 玻璃")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 玻璃")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 玻璃")
                imok=0
        elif firstquestion==114 and imok==1 :
            if eny1.get()=="鞋子" :
                if hintq1==0 and hintq2==0 :
                    imok=0
                    answerr.configure(text="A: 鞋子")
                    user+=3
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 and hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 鞋子")
                    user+=1
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
                elif hintq1==1 or hintq2==1 :
                    imok=0
                    answerr.configure(text="A: 鞋子")
                    user+=2
                    scores.configure(text=""+str(user))
                    hintq1=0
                    hintq2=0
            else :
                answerr.configure(text="A: 鞋子")
                imok=0        
            
user=0 #user是答對總分數的變數名稱
firstquestion=0 #firstquestion是電腦隨機抽出的題目
start=0 #start變數名稱是做為"開始這一輪"猜燈謎，0為還沒 1為開始這一輪，如果結束猜燈謎的話要記得案清除按鈕，這樣才會歸0，下次才能再開始猜，並且代表下一輪計分
imok=0 #imok變數名稱是做為防止確定答案刷分意思，只有點開始/新題目才會變成1，其餘不會，就是怕之後再按確定按鈕時出現刷分現象，然後每次題目答案審查完都會歸0，
       #0為未開啟 1為開啟意思
hintq1=0 #hintq1代表提示1，0就是該題目目前沒有用提示1 1就是該題目目前用了提示1的意思，方便如果你用了提示1的標記
hintq2=0 #hintq2代表提示2，0就是該題目目前沒有用提示2 1就是該題目目前用了提示2的意思，方便如果你用了提示2的標記
plt.rcParams["font.sans-serif"]="Microsoft JhengHei" #最一開始run時，直接針對接下來後續該程式碼板子上的figure()指令產生的圖表，或該板子上系統給的圖表直接改成該預設字形->有中英文及數字字形
window=s.Tk()
window.title("猜燈謎")
window.geometry("730x300") #該置放點為大小及出現在螢幕位置的參數 600x300是大小方面 出現在螢幕這邊沒設
window.resizable(0,0)
bb=s.StringVar()
rb1=s.Radiobutton(window,text="幽默冷笑話類",variable=bb,value="幽默冷笑話",command=s1)
rb2=s.Radiobutton(window,text="食物和水果類",variable=bb,value="食物和水果",command=s2)
rb3=s.Radiobutton(window,text="文學造詣類",variable=bb,value="文學造詣",command=s3)
rb4=s.Radiobutton(window,text="猜數字類",variable=bb,value="數字",command=s4)
rb5=s.Radiobutton(window,text="物品跟用品及工具類",variable=bb,value="物品跟用品及工具類",command=s5)
lb1=s.Label(window,text="Q:")
answer=s.Label(window,text="->")
lb2=s.Label(window,text="")
lb3=s.Label(window,text="")
eny1=s.Entry(window,width=25)
first=s.Button(window,text="開始/下一題",width=10,command=firststart)
clear=s.Button(window,text="清除",width=10,command=clears)
sure=s.Button(window,text="確定",width=10,command=suretosure)
answerr=s.Label(window,text="A: ")
bt2=s.Button(window,text="提示1",width=7,command=hint1)
bt3=s.Button(window,text="提示2",width=7,command=hint2)
lb4=s.Label(window,text="提示1")
lb5=s.Label(window,text="提示2")
lb6=s.Label(window,text="Score:",font=("標楷體",12),bg="yellow",width=7,height=1)
                       #bg是背景顏色關鍵字變數名稱參數，他的輸入值可以用她背景顏色的代碼or直接輸入顏色也可
scores=s.Label(window,text="0")
bt5=s.Button(window,text="出題率",width=10,command=p)
bt4=s.Button(window,text="規則介紹",width=10,command=introductions)
rb1.place(x=20,y=20)
rb2.place(x=130,y=20)
rb3.place(x=20,y=50)
rb4.place(x=130,y=50)
rb5.place(x=20,y=80)
lb1.place(x=300,y=30)
answer.place(x=300,y=100)
lb2.place(x=320,y=30)
lb3.place(x=320,y=60)
eny1.place(x=320,y=100)
first.place(x=70,y=120)
clear.place(x=70,y=150)
sure.place(x=520,y=95)
answerr.place(x=450,y=130)
bt2.place(x=320,y=150)
bt3.place(x=320,y=175)
lb4.place(x=390,y=155)
lb5.place(x=390,y=180)
lb6.place(x=20,y=270)
scores.place(x=80,y=272)
bt5.place(x=520,y=270)
bt4.place(x=610,y=270)
window.mainloop()