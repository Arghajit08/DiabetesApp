from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import joblib

def home(request):
    return render(request,"index.html")
def result(request):
    lis=[]
    name=request.GET['name']
    lis.append(request.GET['P'])
    lis.append(request.GET['G'])
    lis.append(request.GET['B'])
    lis.append(request.GET['S'])
    lis.append(request.GET['I'])
    lis.append(request.GET['BM'])
    lis.append(request.GET['D'])
    lis.append(request.GET['A'])

    datasets={'Pregnancies':lis[0],'Glucose':lis[1],'BloodPressure':lis[2],'SkinThickness':lis[3],'Insulin':lis[4],'BMI':lis[5],'DiabetesPedigreeFunction':lis[6],'Age':lis[7]}
    
    print(datasets)
    
    userinput=pd.DataFrame(datasets,index=[0])
    
    print(userinput)
    model=joblib.load("model.sav")
    ans=model.predict(userinput)
    print(ans)
    if(ans==[0]):
        x="not diabetic"
    elif(ans==[1]):
        x="Diabetic"
    print(x)
    return render(request,"result.html",{'name':name,'ans':x,'preg':lis[0],'glu':lis[1],'bp':lis[2],'st':lis[3],'ins':lis[4],'bmi':lis[5],'dpf':lis[6],'age':lis[7]})