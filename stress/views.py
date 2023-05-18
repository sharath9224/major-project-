from django.shortcuts import render
from django.http import HttpResponse
from stress.models import StressDetection




from joblib import load
data1=load('./MLMODEL/model.joblib')
transform=load('./MLMODEL/model2.joblib')



def new_1(request):
    return render(request,'new 1.html')

def about_us(request):
    return render(request,'work.html')

def click_here(request):
    return render(request,'ques.html')

def data(request):
    ques1=request.POST.get('question4')
    ques2=request.POST.get('When')
    ques3=request.POST.get('question6')
    ques4=request.POST.get('question7')
    ques5=request.POST.get('question8')
    ques6=request.POST.get('find')
    ques7=request.POST.get('spend')
    ques8=request.POST.get('goal')
    ques9=request.POST.get('learn')
    ques13=request.POST.get('work')
    print(ques1,ques2,ques3,ques4,ques5,ques6,ques7,ques8,ques9,ques13)
    stress=[[ques1,ques2,ques3,ques4,ques5,ques6,ques7,ques8,ques9,ques13]]
    print(stress)
    y=transform.transform(stress)
    y_pred=data1.predict(y)
    y_pred=y_pred[0]
    # print(y_pred)


    if y_pred==0.0:
        y_pred='LOW STRESS'
        
    if y_pred==1.0:
        y_pred='MODERATE STRESS'
    if y_pred==2.0:
        y_pred='HIGH STRESS'


    context={
        'y':y_pred
    }
    


    
    

    ins=StressDetection(question1=ques1,
    question2=ques2,
    question3=ques3,
    question4=ques4,
    question5=ques5,
    question6=ques6,
    question7=ques7,
    question8=ques8,
    question9=ques9,
    question13=ques13
    )

    ins.save()

    
    return render(request,'ques.html',context)

     
