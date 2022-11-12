from flask import Flask,render_template,request
import os, os.path
from better_profanity import profanity

profanity.load_censor_words()

app = Flask(__name__)

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])

def home():
    text ="s-t/est"
    uname ="uname-t/est"
    psw ="psw-t/est"
    signuname ="signuname-t/est"
    signpsw ="signpsw-t/est"
    sta='n'
    if request.method == 'POST':
        if 'text' in request.form:
            text =request.form['text'];
        if 'uname' in request.form:
            uname =request.form['uname'];
        if 'psw' in request.form:
            psw =request.form['psw'];
        if 'sta' in request.form:
            sta =request.form['sta'];
            
        if 'signuname' in request.form:
            signuname =request.form['signuname'];
        if 'signpsw' in request.form:
            signpsw =request.form['signpsw'];
        
    Textlog=[]
    if(signuname!="signuname-t/est" and signpsw !="signpsw-t/est"):
        file = open('./static/files/userpas.txt','a', encoding='utf-8')
        file.write("ID:"+signuname+"-"+"PA:"+signpsw+"\n")
        filestatus = open('./static/files/userstatus.txt','a', encoding='utf-8')
        filestatus.write("ID:"+signuname+"-"+"status:"+"0"+"\n")
        file.close
        filestatus.close
    if(uname!="uname-t/est" and psw !="psw-t/est"):
        fileL = open('./static/files/userpas.txt','r', encoding='utf-8')
        getlog = fileL.read()
        listlog = getlog.split("\n")
        check=("ID:"+uname+"-"+"PA:"+psw)
      
        for i in range(len(listlog)):
            if(check==listlog[i]):
              
                usershow=uname
                fileban = open("./static/files/userban.txt", encoding='utf-8')
                string_ban = fileban.readlines()
                userdban = "ID:"+usershow+"\n"
                print("userdban", userdban)
                for j in range(len(string_ban)):
                    if(userdban == string_ban[j]):
                        print("true")
                        return render_template('index.html')
                    else:
                        print("falue")
                print("usershow", usershow)
                print("string_ban", string_ban)
                fileban.close
                
                
                filestatus = open("./static/files/userstatus.txt", encoding='utf-8')
                string_list = filestatus.readlines()
                filestatus.close
             
                for j in range(len(listlog)):
                    if(check==listlog[i]):
                        string_list[i] = ("ID:"+uname+"-"+"status:"+"1"+"\n")
                my_file = open("./static/files/userstatus.txt", "w", encoding='utf-8')
                new_file_contents = "".join(string_list)
                my_file.write(new_file_contents)
                my_file.close()
                readable_file = open("./static/files/userstatus.txt", encoding='utf-8')
                read_file = readable_file.read()
                dotall=[]
                nuball=[]
                listText=[]
                nubUse=[]
                Nspaceall=[]
                f = open("./static/files/texttest.txt", "r" ,encoding='utf-8')
                article = f.read()
                getlist = article.split("\n")
                for i in range(len(getlist)):
                    dotall.append(str(getlist[i])+"-")
                Joinall=(''.join(dotall))
                censorJall = profanity.censor(Joinall)
                splall=censorJall.split("-")
                print(Joinall)
                print(splall)
            
                for i in range(len(splall)):
                    if(splall[i]!=''):
                        nuball.append(i)
                        Nspaceall.append(splall[i])


                    if(splall[i]!=uname):
                        if(i%2==0):
                            if(splall[i+1]!=''):
                                listText.append(splall[i+1]+",-")
                    else:
                        nubUse.append(i+1)

                textall=[]
                for i in range(len(nuball)):
                    textall.append(str(nuball[i])+",-")
                Jointextall=(''.join(textall))

                textnubUse=[]
                for i in range(len(nubUse)):
                    textnubUse.append(str(nubUse[i])+",-")
                JointextnubUse=(''.join(textnubUse))
                
                textNspaceall=[]
                for i in range(len(Nspaceall)):
                    textNspaceall.append(str(Nspaceall[i])+",-")
                JointexttextNspaceall=(''.join(textNspaceall))
                print(Jointextall)
                print(JointextnubUse)
                
                t="Hi"
                if(uname=="admin"):
                    return render_template('admin.html',txtread=t,shuser=usershow,tuse=JointextnubUse,tall=JointexttextNspaceall)
                return render_template('loginn.html',txtread=t,shuser=usershow,tuse=JointextnubUse,tall=JointexttextNspaceall)
            else:
                print("NO "+listlog[i])

    def readtex():
        listText=[]
        dotalls=[]
        f = open("./static/files/texttest.txt", "r" ,encoding='utf-8')
        article = f.read()
        getlist = article.split("\n")
        

        for i in range(len(getlist)):
            dotalls.append(str(getlist[i])+"-")
        Joinall=(''.join(dotalls))
        splall=Joinall.split("-")
            
        for i in range(len(splall)):
            if(i<len(splall)-1):
                
                listText.append(splall[i]+",-")
        Joinallss=(''.join(listText))
        print(Joinallss)
        return(Joinallss)
    
    textall=readtex()    
    t="Hi"
    return render_template('index.html',txtread=textall)
'''
    if(sta!='n'):
        if(text!="s-t/est"):
            def writetex():
                censortext = profanity.censor(text)
                file = open('./static/files/texttest.txt','a', encoding='utf-8')
                file.write("\n"+censortext)
                file.close
        
            def readtex():
                listText=[]
                f = open("./static/files/texttest.txt", "r" ,encoding='utf-8')
                article = f.read()
                getlist = article.split("\n")
                for i in range(len(getlist)):
                    if(i<len(getlist)-1):
                        listText.append(getlist[i]+",-")
            
                Jointxt=(''.join(listText))
                print(Jointxt)
                return(Jointxt)

            writetex();
            textread=readtex()  
       
            return render_template('index.html',txts=text,txtread=textread)
        else:
            t="Hi"
            return render_template('index.html',txtread=t)
    else:
        
        t="Hi"
        return render_template('index.html',txtread=t)'''

@app.route('/logn', methods=['GET',"POST"])
def logn():
    text ="s-t/est"
    dottext=[]
    fileO = open('./static/files/userstatus.txt','r', encoding='utf-8')
    getO = fileO.read()
    listO = getO.split("\n")
    for i in range(len(listO)):
        dottext.append(str(listO[i])+"-")
    Joindottext=(''.join(dottext))
  
                
    tq=Joindottext.split("-")
    for i in range(len(tq)):
        if(tq[i]=="status:1"):
            getone=tq[i-1]
            getIndexOne=i-1
    

    splitgetone=getone.split(":")
    selectname=splitgetone[1]
    
        
    if request.method == 'POST':
        if 'text' in request.form:
            text =request.form['text'];
        if 'out' in request.form:
            out =request.form['out'];
            if(out=='0'):
                usershow=selectname
                filestatus = open("./static/files/userstatus.txt", encoding='utf-8')
                string_list = filestatus.readlines()
                filestatus.close
              
                for j in range(len(string_list)):
                
                    checkone="ID:"+selectname+"-"+"status:1\n"
                   
                    if(string_list[j]==checkone):
                      
                        string_list[j] = ("ID:"+selectname+"-"+"status:"+"0"+"\n")
                    else:
                        print("Nooout")
                my_file = open("./static/files/userstatus.txt", "w", encoding='utf-8')
                new_file_contents = "".join(string_list)
                my_file.write(new_file_contents)
                my_file.close()

                def readtex():
                    listText=[]
                    dotalls=[]
                    censortext = profanity.censor(text)
                    f = open("./static/files/texttest.txt", "r" ,encoding='utf-8')
                    article = f.read()
                    getlist = article.split("\n")
        

                    for i in range(len(getlist)):
                        dotalls.append(str(getlist[i])+"-")
                    Joinall=(''.join(dotalls))
                    splall=Joinall.split("-")
            
                    for i in range(len(splall)):
                        if(i<len(splall)-1):
                
                            listText.append(splall[i]+",-")
                    Joinallss=(''.join(listText))
                    print(Joinallss)
                    return(Joinallss)
    
                textall=readtex()    
              
                 
               
                return render_template('index.html',txtread=textall)

     
    if(text!="s-t/est"):
         
        def writetex():
            censortext = profanity.censor(text)
            file = open('./static/files/texttest.txt','a', encoding='utf-8')
            file.write(selectname+"-"+censortext+"\n")
            file.close
           
            userlog = open('./static/files/'+selectname+'.txt','a', encoding='utf-8')
            userlog.write(selectname+"-"+text+"\n")
           
            userlog.close
        
        def readtex():
            dotall=[]
            listText=[]
            nuball=[]
            Nspaceall=[]
            nubUse=[]
            f = open("./static/files/texttest.txt", "r" ,encoding='utf-8')
            article = f.read()
            getlist = article.split("\n")
            
            
            for i in range(len(getlist)):
                dotall.append(str(getlist[i])+"-")
            Joinall=(''.join(dotall))
            splall=Joinall.split("-")
            
            for i in range(len(splall)):
                if(splall[i]!=''):
                    nuball.append(i)
                    Nspaceall.append(splall[i])


                if(splall[i]!=selectname):
                    if(i%2==0):
                        if(splall[i+1]!=''):
                            listText.append(splall[i+1]+",-")
                else:
                    nubUse.append(i+1)

            textall=[]
            for i in range(len(nuball)):
                textall.append(str(nuball[i])+",-")
            Jointextall=(''.join(textall))

            textnubUse=[]
            for i in range(len(nubUse)):
                textnubUse.append(str(nubUse[i])+",-")
            JointextnubUse=(''.join(textnubUse))

            textNspaceall=[]
            for i in range(len(Nspaceall)):
                textNspaceall.append(str(Nspaceall[i])+",-")
            JointexttextNspaceall=(''.join(textNspaceall))
        
            print(Jointextall)
            print(JointextnubUse)
            print(JointexttextNspaceall)
            
            Jointxt=(''.join(listText))
         
            
        
            dotU=[]
            textMe=[]
            
            u = open("./static/files/"+selectname+".txt", "r" ,encoding='utf-8')
            articleu = u.read()
            getlistu = articleu.split("\n")
            censorarticleu = profanity.censor(articleu)
            censorgetlistu = censorarticleu.split("\n")
            
            
            
        
            print ("censorgetlistu", censorgetlistu)
            
                
            for i in range(len(getlistu)):
                dotU.append(str(getlistu[i])+"-")
            JoinU=(''.join(dotU))
            splu=JoinU.split("-")

            
            
            for i in range(len(splu)):
                if(splu[i]==selectname):
                    textMe.append(splu[i+1]+",-")
            JoinMe=(''.join(textMe))
            return(Jointxt,JoinMe,JointextnubUse,JointexttextNspaceall)


        writetex();
        textread,textMread,textuse,textal=readtex()  
        u = open("./static/files/"+selectname+".txt", "r" ,encoding='utf-8')
        articleu = u.read()
        getlistu = articleu.split("\n")
        censorarticleu = profanity.censor(articleu)
        censorgetlistu = censorarticleu.split("\n")
        numberban = 0
        for i in range(len(censorgetlistu)):
                if( "****" in censorgetlistu[i]):
                    numberban += 1
        if(numberban >= 3):
            file = open('./static/files/userban.txt','a', encoding='utf-8')
            file.write("ID:"+selectname+"\n")
            
            file.close
            
            return render_template('index.html')
        else:
            return render_template('loginn.html',txts=textMread,txtread=textread,shuser=selectname,tuse=textuse,tall=textal)
    else:
        
        t="Hi,-"
        return render_template('loginn.html',txtread=t)

@app.route('/admin', methods=['GET',"POST"])
def admin():
    text ="s-t/est"
    dottext=[]
    fileO = open('./static/files/userstatus.txt','r', encoding='utf-8')
    getO = fileO.read()
    listO = getO.split("\n")
    for i in range(len(listO)):
        dottext.append(str(listO[i])+"-")
    Joindottext=(''.join(dottext))
  
                
    tq=Joindottext.split("-")
    for i in range(len(tq)):
        if(tq[i]=="status:1"):
            getone=tq[i-1]
            getIndexOne=i-1
    

    splitgetone=getone.split(":")
    selectname=splitgetone[1]
    
        
    if request.method == 'POST':
        if 'text' in request.form:
            text =request.form['text'];
        if 'out' in request.form:
            out =request.form['out'];
            if(out=='0'):
                usershow=selectname
                filestatus = open("./static/files/userstatus.txt", encoding='utf-8')
                string_list = filestatus.readlines()
                filestatus.close
              
                for j in range(len(string_list)):
                
                    checkone="ID:"+selectname+"-"+"status:1\n"
                   
                    if(string_list[j]==checkone):
                      
                        string_list[j] = ("ID:"+selectname+"-"+"status:"+"0"+"\n")
                    else:
                        print("Nooout")
                my_file = open("./static/files/userstatus.txt", "w", encoding='utf-8')
                new_file_contents = "".join(string_list)
                my_file.write(new_file_contents)
                my_file.close()

                def readtex():
                    listText=[]
                    dotalls=[]
                    f = open("./static/files/texttest.txt", "r" ,encoding='utf-8')
                    article = f.read()
                    getlist = article.split("\n")
        

                    for i in range(len(getlist)):
                        dotalls.append(str(getlist[i])+"-")
                    Joinall=(''.join(dotalls))
                    splall=Joinall.split("-")
            
                    for i in range(len(splall)):
                        if(i<len(splall)-1):
                
                            listText.append(splall[i]+",-")
                    Joinallss=(''.join(listText))
                    print(Joinallss)
                    return(Joinallss)
    
                textall=readtex()    
              
                 
               
                return render_template('index.html',txtread=textall)

     
    if(text!="s-t/est"):
         
        def writetex():
            censortext = profanity.censor(text)
            file = open('./static/files/texttest.txt','a', encoding='utf-8')
            file.write(selectname+"-"+censortext+"\n")
            file.close
           
            userlog = open('./static/files/'+selectname+'.txt','a', encoding='utf-8')
            userlog.write(selectname+"-"+text+"\n")
           
            userlog.close
        
        def readtex():
            dotall=[]
            listText=[]
            nuball=[]
            Nspaceall=[]
            nubUse=[]
            f = open("./static/files/texttest.txt", "r" ,encoding='utf-8')
            article = f.read()
            getlist = article.split("\n")
            for i in range(len(getlist)):
                dotall.append(str(getlist[i])+"-")
            Joinall=(''.join(dotall))
            splall=Joinall.split("-")
            
            for i in range(len(splall)):
                if(splall[i]!=''):
                    nuball.append(i)
                    Nspaceall.append(splall[i])


                if(splall[i]!=selectname):
                    if(i%2==0):
                        if(splall[i+1]!=''):
                            listText.append(splall[i+1]+",-")
                else:
                    nubUse.append(i+1)

            textall=[]
            for i in range(len(nuball)):
                textall.append(str(nuball[i])+",-")
            Jointextall=(''.join(textall))

            textnubUse=[]
            for i in range(len(nubUse)):
                textnubUse.append(str(nubUse[i])+",-")
            JointextnubUse=(''.join(textnubUse))

            textNspaceall=[]
            for i in range(len(Nspaceall)):
                textNspaceall.append(str(Nspaceall[i])+",-")
            JointexttextNspaceall=(''.join(textNspaceall))
        
            print(Jointextall)
            print(JointextnubUse)
            print(JointexttextNspaceall)
            
            Jointxt=(''.join(listText))
         
            
        
            dotU=[]
            textMe=[]
            u = open("./static/files/"+selectname+".txt", "r" ,encoding='utf-8')
            articleu = u.read()
            getlistu = articleu.split("\n")
            for i in range(len(getlistu)):
                dotU.append(str(getlistu[i])+"-")
            JoinU=(''.join(dotU))
            splu=JoinU.split("-")
          
            for i in range(len(splu)):
                if(splu[i]==selectname):
                    textMe.append(splu[i+1]+",-")
            JoinMe=(''.join(textMe))
            return(Jointxt,JoinMe,JointextnubUse,JointexttextNspaceall)


        writetex();
        textread,textMread,textuse,textal=readtex()  
   
        return render_template('admin.html',txts=textMread,txtread=textread,shuser=selectname,tuse=textuse,tall=textal)
    else:
        
        def readtex():
            dotall=[]
            listText=[]
            nuball=[]
            Nspaceall=[]
            nubUse=[]
            f = open("./static/files/texttest.txt", "r" ,encoding='utf-8')
            article = f.read()
            getlist = article.split("\n")
            for i in range(len(getlist)):
                dotall.append(str(getlist[i])+"-")
            Joinall=(''.join(dotall))
            splall=Joinall.split("-")
            
            for i in range(len(splall)):
                if(splall[i]!=''):
                    nuball.append(i)
                    Nspaceall.append(splall[i])


                if(splall[i]!=selectname):
                    if(i%2==0):
                        if(splall[i+1]!=''):
                            listText.append(splall[i+1]+",-")
                else:
                    nubUse.append(i+1)

            textall=[]
            for i in range(len(nuball)):
                textall.append(str(nuball[i])+",-")
            Jointextall=(''.join(textall))

            textnubUse=[]
            for i in range(len(nubUse)):
                textnubUse.append(str(nubUse[i])+",-")
            JointextnubUse=(''.join(textnubUse))

            textNspaceall=[]
            for i in range(len(Nspaceall)):
                textNspaceall.append(str(Nspaceall[i])+",-")
            JointexttextNspaceall=(''.join(textNspaceall))
        
            print(Jointextall)
            print(JointextnubUse)
            print(JointexttextNspaceall)
            
            Jointxt=(''.join(listText))
         
            
        
            dotU=[]
            textMe=[]
            u = open("./static/files/"+selectname+".txt", "r" ,encoding='utf-8')
            articleu = u.read()
            getlistu = articleu.split("\n")
            for i in range(len(getlistu)):
                dotU.append(str(getlistu[i])+"-")
            JoinU=(''.join(dotU))
            splu=JoinU.split("-")
          
            for i in range(len(splu)):
                if(splu[i]==selectname):
                    textMe.append(splu[i+1]+",-")
            JoinMe=(''.join(textMe))
            return(Jointxt,JoinMe,JointextnubUse,JointexttextNspaceall)


        textread,textMread,textuse,textal=readtex()  
   
        return render_template('admin.html',txts=textMread,txtread=textread,shuser=selectname,tuse=textuse,tall=textal)
    

@app.route('/setting', methods=['GET',"POST"])
def setting():   
    dottext=[]
    getuser=[]
    fileO = open('./static/files/userstatus.txt','r', encoding='utf-8')
    getO = fileO.read()
    listO = getO.split("\n")
    looktext="-,test"
    if 'out' in request.form:
        out =request.form['out'];
        print(request.form)

        def readUSer():
            listText=[]
            checkfile=out+".txt"
            statcheck=0
            DIR = './static/files'
            filesname = (([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
            for i in range(len(filesname)):
                if(checkfile == filesname[i]):
                    statcheck=1
                    
            if(statcheck==1):
                
                f = open("./static/files/"+out+".txt", "r" ,encoding='utf-8')
                article = f.read()
                getlist = article.split("\n")
                censorarticle = profanity.censor(article)
                censorgetlist = censorarticle.split("\n")
                print("censorgetlist", censorgetlist)
                print(getlist[0])
               
                censortext = []
                textsend=[]
                numberban = 0
                for i in range(len(getlist)):
                    if(getlist[i]!=''):
                        if (getlist[i] != censorgetlist[i]):
                            textsend.append("*** CENSOR WORDS *** --> ")
                            numberban += 1
                            
                    textsend.append(str(getlist[i])+",-")     
                        
                         
                        
                print("censortext", censortext)
                print("textsend", textsend)
                print("numberban", numberban)
                Jointextsend=(''.join(textsend))
                
                
                print(Jointextsend)
                return(Jointextsend)
            else:
                getlist="User has not sent a message."
                return(getlist)
            
        looktext=readUSer()
        print(looktext)
    for i in range(len(listO)):
        dottext.append(str(listO[i])+"-")
    Joindottext=(''.join(dottext))
    print
                
    tq=Joindottext.split("-")
    for i in range(len(tq)):
        if(tq[i]=="status:1"):
            getone=tq[i-1]
            getIndexOne=i-1
        
        if(tq[i]!="status:1" and tq[i]!="status:0" ):
            if(tq[i]!="ID:admin" and tq[i]!="" ):
                getuser.append(tq[i])
        
    splitgetone=getone.split(":")
    selectname=splitgetone[1]
    useralls=[]
    for i in range(len(getuser)):
        useralls.append(str(getuser[i])+",-")
    Joinuseralls=(''.join(useralls))

    splituseralls=Joinuseralls.split(":")
    Luseralls=[]
    for i in range(len(splituseralls)):
        Luseralls.append(str(splituseralls[i])+",-")
    JoinuLuserall=(''.join(Luseralls))
    
    print("JoinuLuserall", JoinuLuserall)
    print("looktext", looktext)
    
    uban = open("./static/files/userban.txt", "r" ,encoding='utf-8')
    articleuban = uban.read()
    getlistarticleuban = articleuban.split("\n")
    print("getlistarticleuban", getlistarticleuban)
    Larticleuban = []
    for i in range(len(getlistarticleuban)):
        if(getlistarticleuban[i] != ''):
            Larticleuban.append(str(getlistarticleuban[i])+",-")
    Joingetlistarticleuban = (''.join(Larticleuban))
    print("Joingetlistarticleuban", Joingetlistarticleuban)
    
    if(looktext=="-,test"):
        return render_template('setting.html',shuser=selectname,allu=JoinuLuserall, alluban=Joingetlistarticleuban)
    else:
        return render_template('setting.html',shuser=selectname,allu=JoinuLuserall,lookT=looktext, alluban=Joingetlistarticleuban)
    
    
if __name__ == "__main__":
    app.run(debug=True)