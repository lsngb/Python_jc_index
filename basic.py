import tkinter as tk
import data

class gui():
    def __init__(self):
#setup window
        self.root = tk.Tk()
        self.root.title("集成曲谱曲牌检索 v1.0")
        self.root.configure(bg="#f3df99")
        X = int(self.root.winfo_screenwidth())-800
        Y = int(self.root.winfo_screenheight())-600
        self.root.minsize(785,520)
        self.root.geometry("785x520+%d+%d" % (X/2 , Y/2))
#title frame
        self.titleframe=tk.Frame(self.root)
        self.titleframe.grid(row=0,column=0,columnspan=8,sticky="W",padx=60)
        self.titleframe.config(bg="#f3df99")

        self.labelA=tk.Label(self.titleframe,text="集成曲谱曲牌检索",font=("ss","13","bold"))
        self.labelA.grid(row=0,column=0,columnspan=4,pady=20)
        self.labelA.configure(background="#f3df99")
        self.labelB=tk.Label(self.titleframe,text="根据《螾庐曲谈·卷三》整理录入 by 乱煞年光遍")
        self.labelB.configure(background="#f3df99")
        self.labelB.grid(row=1,column=1,columnspan=5,padx=40)

#search frame
        self.searchframe=tk.Frame(self.root)
        self.searchframe.grid(row=1,column=0,pady=15,columnspan=8,padx=10)
        self.searchframe.config(bg="#f3df99")
        
        self.label1=tk.Label(self.searchframe,text="宫调",width=12)
        self.label1.configure(background="#f3df99")
        self.label1.grid(row=3,column=1)
        self.label2=tk.Label(self.searchframe,text="性质",width=12)
        self.label2.configure(background="#f3df99")
        self.label2.grid(row=3,column=2)
        self.label3=tk.Label(self.searchframe,text="曲牌",width=12)
        self.label3.configure(background="#f3df99")
        self.label3.grid(row=3,column=3)
        self.label3=tk.Label(self.searchframe,text="剧目",width=12)
        self.label3.configure(background="#f3df99")
        self.label3.grid(row=3,column=4)
        self.label4=tk.Label(self.searchframe,text="折子",width=12)
        self.label4.configure(background="#f3df99")
        self.label4.grid(row=3,column=5)
        self.label5=tk.Label(self.searchframe,text="位置",width=12)
        self.label5.configure(background="#f3df99")
        self.label5.grid(row=3,column=6)
                
        self.entry1=tk.Entry(self.searchframe,width=10)
        self.entry1.grid(row=4,column=1)
        self.entry2=tk.Entry(self.searchframe,width=10)
        self.entry2.grid(row=4,column=2)
        self.entry3=tk.Entry(self.searchframe,width=10)
        self.entry3.grid(row=4,column=3)
        self.entry4=tk.Entry(self.searchframe,width=10)
        self.entry4.grid(row=4,column=4)
        self.entry5=tk.Entry(self.searchframe,width=10)
        self.entry5.grid(row=4,column=5)
        self.entry6=tk.Entry(self.searchframe,width=10)
        self.entry6.grid(row=4,column=6)
#searchbutton
        self.button=tk.Button(self.searchframe,text="  搜　 索  ",width=8,command=lambda: self.searchdata(self.entry1.get(),self.entry2.get(),self.entry3.get(),self.entry4.get(),self.entry5.get(),self.entry6.get()))
        self.button.config(bg="#814713",fg="white")
        self.button.grid(row=3,column=7,sticky="W"+"S",rowspan=2,padx=25)
        
#example frame
        self.exframe=tk.Frame(self.root)
        self.exframe.grid(row=2,column=0,columnspan=20,pady=40,padx=34,rowspan=9)
        self.exframe.config(bg="#f3df99")
        
        self.flabel00=tk.Label(self.exframe,text="示例",font=("ss","11","bold"),width=15)
        self.flabel00.configure(bg="#f3df99")
        self.flabel00.grid(row=0,column=0,sticky="W")
        self.flabel0=tk.Label(self.exframe,text="序号	宫调	性质	曲牌	剧目	折子	位置",width=58)
        self.flabel0.configure(bg="#f3df99")
        self.flabel0.grid(row=1,column=0,sticky="W",pady=5)
        self.flabel1=tk.Label(self.exframe,text="0010	仙吕宫	南引子	番卜算	燕子笺	拾笺	振五",width=58)
        self.flabel1.configure(bg="#f3df99")
        self.flabel1.grid(row=2,column=0,sticky="W")
        self.flabel1=tk.Label(self.exframe,text="0044	仙吕宫	南过曲	月儿高	白罗衫	游园	振八",width=58)
        self.flabel1.configure(bg="#f3df99")
        self.flabel1.grid(row=3,column=0,sticky="W")
        self.flabel1=tk.Label(self.exframe,text="0061	仙吕宫	南过曲	醉扶归	牡丹亭	游园	声四",width=58)
        self.flabel1.configure(bg="#f3df99")
        self.flabel1.grid(row=4,column=0,sticky="W")
        self.flabel3=tk.Label(self.exframe,text="0372	南吕宫	南过曲	一江风	西楼记	拆书	金六",width=58)
        self.flabel3.configure(bg="#f3df99")
        self.flabel3.grid(row=5,column=0,sticky="W")       
        self.flabel4=tk.Label(self.exframe,text="0373	南吕宫	南过曲	一江风	荆钗记	绣房	声二",width=58)
        self.flabel4.configure(bg="#f3df99")
        self.flabel4.grid(row=6,column=0,sticky="W")
        self.flabel5=tk.Label(self.exframe,text="0500	南吕宫	南集曲	罗江怨	西楼记	楼会	金六",width=58)
        self.flabel5.configure(bg="#f3df99")
        self.flabel5.grid(row=7,column=0,sticky="W")
        self.flabel5=tk.Label(self.exframe,text="0534	南吕宫	北曲	乌夜啼	铁冠图	守门	玉六",width=58)
        self.flabel5.configure(bg="#f3df99")
        self.flabel5.grid(row=8,column=0,sticky="W")
#picture
        photo=tk.PhotoImage(file="pic.asd")
        self.labelp=tk.Label(self.exframe,image=photo)
        self.labelp.image = photo
        self.labelp.configure(background="#f3df99")
        self.labelp.grid(row=0,column=1,sticky="N"+"W",pady=10,rowspan=50,padx=20)


    def MainLoop(self):
        self.root.mainloop()


    def searchdata(self,a,b,c,d,e,f):
        self.clear()
        a=str(a)
        b=str(b)
        c=str(c)
        d=str(d)
        e=str(e)
        f=str(f)
#textframe
        self.textframe=tk.Frame(self.root)
        self.textframe.grid(row=2,column=0,rowspan=20,columnspan=20,padx=45)
        self.textframe.configure(bg="#f3df99")
        
        self.text=tk.Text(self.textframe,width=57,height=25)
        self.text.grid(row=1,column=0,columnspan=8)
        self.scrollbar=tk.Scrollbar(self.textframe)
        self.scrollbar.grid(row=1,column=8,sticky="N"+"S")
        self.scrollbar.config(command=self.text.yview,troughcolor="#814713")
        self.text.config(yscrollcommand=self.scrollbar.set,bg="#f3e7bf")
        self.labelaa=tk.Label(self.textframe,text="序  号")
        self.labelaa.grid(row=0,column=0,sticky="W")
        self.labelaa.config(bg="#f3df99")
        self.labela=tk.Label(self.textframe,text="  宫  调")
        self.labela.grid(row=0,column=1,sticky="W")
        self.labela.config(bg="#f3df99")
        self.labelb=tk.Label(self.textframe,text="性  质")
        self.labelb.grid(row=0,column=2,sticky="W")
        self.labelb.config(bg="#f3df99")
        self.labelc=tk.Label(self.textframe,text=" 曲  牌")
        self.labelc.grid(row=0,column=3,sticky="W")
        self.labelc.config(bg="#f3df99")
        self.labele=tk.Label(self.textframe,text="剧  目")
        self.labele.grid(row=0,column=4,sticky="W")
        self.labele.config(bg="#f3df99")
        self.labeld=tk.Label(self.textframe,text="折子  ")
        self.labeld.grid(row=0,column=5,sticky="W")
        self.labeld.config(bg="#f3df99")
        self.labele=tk.Label(self.textframe,text="位置")
        self.labele.grid(row=0,column=6,sticky="W")
        self.labele.config(bg="#f3df99")
#picture
        photo=tk.PhotoImage(file="pic.asd")
        self.labelp=tk.Label(self.textframe,image=photo)
        self.labelp.image = photo
        self.labelp.configure(background="#f3df99")
        self.labelp.grid(row=0,column=9,sticky="N"+"W",pady=50,rowspan=10,padx=1)
        

        search_dic=data.datas()
        result=search_dic.final(a,b,c,d,e,f)
        for ele in result:
            for item in ele[1]:
                item=item+"\t"
                self.text.insert(tk.END,item)
            self.text.insert(tk.END,"\n")
        self.text.config(state="disabled")

            
            
    def clear(self):
        self.exframe.grid_remove()
        self.entry1.delete(0,tk.END)
        self.entry2.delete(0,tk.END)
        self.entry3.delete(0,tk.END)
        self.entry4.delete(0,tk.END)
        self.entry5.delete(0,tk.END)
        self.entry6.delete(0,tk.END)
