class datas:
    def __init__(self):
        self.__dic={}
        self.__gongdiao={}
        self.__xingzhi={}
        self.__qupai={}
        self.__jumu={}
        self.__zhezi={}
        self.__weizhi={}
        self.__final=[]
        f=open("ref.asd","r",encoding="utf-8")
        while True:
            string=f.readline()
            if string=="":
                break
            l=string.split()
            key=l[0]
            self.__dic[key]=l
        f.close()
        
##宫调a
##性质b
##曲牌c
##剧目d
##折子e
##位置f            
    def search_gongdiao(self,a):
        a=str(a)
        if a.strip()=="":
            self.__gongdiao=self.__dic
        else:
            for key in self.__dic:
                if a.strip() in self.__dic[key][1]:
                    self.__gongdiao[key]=self.__dic[key]
        return self.__gongdiao
    def search_xingzhi(self,a,b):
        gongdiao=self.search_gongdiao(a)
        b=str(b)
        if b.strip()=="":
            self.__xingzhi=gongdiao
        else:
            for key in gongdiao:
                if b.strip() in gongdiao[key][2]:
                        self.__xingzhi[key]=gongdiao[key]
        return self.__xingzhi
    def search_qupai(self,a,b,c):
        xingzhi=self.search_xingzhi(a,b)
        c=str(c)
        if c.strip()=="":
            self.__qupai=xingzhi
        else:
            for key in self.__xingzhi:
                if c.strip() in xingzhi[key][3]:
                    self.__qupai[key]=xingzhi[key]
        return self.__qupai
    def search_jumu(self,a,b,c,d):
        d=str(d)
        qupai=self.search_qupai(a,b,c)
        if d.strip()=="":
            self.__jumu=qupai
        else:
            for key in qupai:
                if d.strip() in qupai[key][4]:
                    self.__jumu[key]=qupai[key]
        return self.__jumu
    def search_zhezi(self,a,b,c,d,e):
        e=str(e)
        jumu=self.search_jumu(a,b,c,d)
        if e.strip()=="":
            self.__zhezi=jumu
        else:
            for key in jumu:
                if e.strip() in jumu[key][5]:
                    self.__zhezi[key]=jumu[key]
        return self.__zhezi
    def search_weizhi(self,a,b,c,d,e,f):
        f=str(f)
        zhezi=self.search_zhezi(a,b,c,d,e)
        if f.strip()=="":
            self.__weizhi=zhezi
        else:
            for key in zhezi:
                if f.strip() in zhezi[key][6]:
                    self.__weizhi[key]=zhezi[key]
        return self.__weizhi
    def final(self,a,b,c,d,e,f):
        weizhi=self.search_weizhi(a,b,c,d,e,f)
        if weizhi=={}:
            weizhi["0"]=["error","没有符合条件的结果"]    
        self.__final=sorted(weizhi.items())
        return self.__final
