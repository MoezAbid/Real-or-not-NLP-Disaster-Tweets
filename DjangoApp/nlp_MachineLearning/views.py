from django.shortcuts import render
from django.shortcuts import render
from sklearn.externals import joblib 
import os
from django.urls import reverse
from django.http import HttpResponseRedirect 
from sklearn.externals import joblib 
from django.utils import timezone
import pandas as pd
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Create your views here.
def predictTweet(request):
    return render(request, './base.html')

def predict(request):
    text= request.POST.get('tweet')
    text=[text]
    #text=["Forest fire near La Ronge Sask. Canada"]

    #vector = joblib.load('count_vectorizer_train1.pkl') 
    #textv=vector.transform(text)
    vectorizer = pickle.load(open("vectorizer.pickle", "rb"))
    question = vectorizer.transform(text)
    print(question.shape)
    model = joblib.load('model.pkl') 
    x=model.predict(question) 
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    print(x)
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    dictionnary = {'result': x[0]}
    
    
    return render(request, './result.html',dictionnary)