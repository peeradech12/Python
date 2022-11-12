from flask import Flask ,render_template,request
import pickle


app = Flask(__name__)


@app.route('/',methods=['GET'])
def hello_word():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    ages= request.form['age'];
    sexs= request.form['sexs'];
    cps= request.form['cp'];
    trestbpss= request.form['trestbps'];
    chols= request.form['chol']
    fbss= request.form['fbs']
    restecgs= request.form['restecg']
    thalachs= request.form['thalach']
    exangs= request.form['exang']
    oldpeaks= request.form['oldpeak']
    slopes= request.form['slope']
    cas= request.form['ca']
    thals= request.form['thal']
    model = pickle.load(open("Ha_model.sav",'rb'))
    
    
    sexs = int(sexs)
    cps = int(cps)
    fbss = int(fbss)
    restecgs = int(restecgs)
    exangs = int(exangs)
    slopes = int(slopes)
    cas = int(cas)
    thals = int(thals)
   
    

    Ans =  model.predict([[ages,sexs,cps,trestbpss,chols,fbss,restecgs,thalachs,exangs,oldpeaks,slopes,cas,thals]] ) 
    
    if(Ans == 1) :
        c =" disease 😷 "
    else :
        c ="no disease 😀"

    if(sexs == 0) :
        gen = "Female"
    else :
        gen = "Male"
    
    if(cps == 0) :
        pain = "typical angina"
    if(cps == 1) :
        pain = "atypical angina"
    if(cps == 2) :
        pain = "non-anginal pain"
    if(cps == 3) :
        pain = "asymptomatic"

    if(fbss == 0) :
        sugar = "false"
    else :
        sugar = "true"

    if(restecgs == 0) :
        ele = "normal"
    if(restecgs == 1) :
        ele = "having ST-T wave abnormality"
    if(restecgs == 2) :
        ele = "howing probable or definite"

    if(exangs == 0) :
        exe = "No"
    else :
        exe = "Yes"

    if(slopes == 0) :
        slo = "upsloping"
    if(slopes == 1) :
        slo = "flat"
    if(slopes == 2) :
        slo = "downsloping"

    if(thals == 0) :
        heart = "normal"
    if(thals == 1) :
        heart= "fixed defect"
    if(thals == 2) :
        heart = "reversible defect"

    text =  "Gender : " + gen + "  |    Age : " + str(ages) 
    testcp = "Chest Pain :" + pain + " | Resting Blood pressure : " + str(trestbpss) + " mmHg"
    textchol = "serum cholesterol : " + str(chols) +" mg/dL"  +  " | fasting blood sugar > 120 mg/d : " +  sugar
    textel ="Resting electrocardiogram results : " + ele + " | heart rate : " + str(thalachs) + " per minute"
    textan = "exercise induced angina : "+exe +" | ST depression induced : " + str(oldpeaks)
    textst ="the slope of the peak exercise ST segment : "+ slo 
    textcas = "number of major vessels (0-3): " + str(cas) +"  |  heart tissue : "+heart
    return render_template('index.html',prediction=c,fiee=text,text2=testcp,test3=textchol,test4=textel,test5=textan,test6=textst,test7=textcas)
    
if __name__ == '__main__':
    app.run(port=3000,debug=True)
