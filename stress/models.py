from django.db import models
#from sklearn.tree import Decisiontreeclassifier
#import joblib
# Create your models here.

class StressDetection(models.Model):
    question1=models.CharField(max_length=10)
    question2=models.CharField(max_length=10)
    question3=models.CharField(max_length=10)
    question4=models.CharField(max_length=10)
    question5=models.CharField(max_length=10)
    question6=models.CharField(max_length=10)
    question7=models.CharField(max_length=10)
    question8=models.CharField(max_length=10)
    question9=models.CharField(max_length=10)
    
    question13=models.CharField(max_length=10)

#model = joblib.load('ML MODEL')

#def save (self, *args, **kwargs):
     #ml_model =joblib.load('ML_MODEL/ml_stress.ipynb')
     #ml_model.predict([self.question1,self.question2,self,question3,self.question4,self.question5,self.question6,self.question7,self.question8,self.question9,self.question10,self.question11,self.question12,self.question13])
     #return super().save(*args,*kwargs)