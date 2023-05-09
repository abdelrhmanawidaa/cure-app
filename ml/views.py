from django.shortcuts import render
from . import predictions
import os
import cv2
import numpy as np
import tensorflow as tf
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.template.response import TemplateResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout




class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name
    


"""
1. The scan function is the main function which is called when the user submits the form.
2. The image is read and passed to the model.
3. The model returns the prediction.
4. The prediction is then passed to the template as a context variable.
5. The template then displays the result. """
@login_required(login_url='signin')
def scan(request):
    message = ""
    prediction = ""
    fss = CustomFileSystemStorage()
    try:
        image = request.FILES["image"]
        print("Name", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" + image.name
        # image details
        image_url = fss.url(_image)
        # Read the image
        imag=cv2.imread(path)
        imag1 = cv2.resize(imag,(300,300))
        X = np.array((imag1[np.newaxis])/255)

        # load model
        model = tf.keras.models.load_model(os.getcwd() + '/dumbs/densenet_bestqwk.h5')
        score_predict=((model.predict(X).ravel()*model.predict(X[:, ::-1, :, :]).ravel()*model.predict(X[:, ::-1, ::-1, :]).ravel()*model.predict(X[:, :, ::-1, :]).ravel())**0.25).tolist()
        label_predict = np.argmax(score_predict)

        # ----------------
        # LABELS
        # 0 - No diabetic retinopathy
        # 1 - Mild
        # 2 - Moderate
        # 3 - Severe
        # 4 - Proliferative diabetic retinopathy
        # ----------------

        
        prediction = label_predict
        print("improtant::  "+str(label_predict))
        if (prediction == 0):
            prediction = "You don't have diabetic retinopathy"
            message = "We’re very happy for you"
        elif (prediction == 1):
            prediction = "Your diabetic retinopathy is Mild"
            message = "We're sorry for you"
        elif (prediction == 2):
             prediction = "Your diabetic retinopathy is Moderate"
             message = "We're sorry for you"
        elif (prediction == 3):
             prediction = "Your diabetic retinopathy is Severe"
             message = "We're sorry for you"
        elif (prediction == 4):
             prediction = "Your diabetic retinopathy is Proliferative"
             message = "We're sorry for you"
        else:
             prediction = "Unknown"
        
         
        
        return TemplateResponse(
            request,
            "result-retin.html",
            {
                "message": message,
                "image": image,
                "image_url": image_url,
                "prediction": prediction,
            },
        )
    except MultiValueDictKeyError:

        return TemplateResponse(
            request,
            "retin-scan-fe.html",
            {"message": "No Image Selected"},
        )

def home(request):
    return render(request,'index.html')

@login_required(login_url='signin')
def earlydiagnosis(request):
    return render(request,'early-diagnosis.html')
    

    """ This code does the following:
1. Takes the input from the form
2. Passes the input to the model
3. Renders the result and a message """

def result(request):
        if request.method == 'POST':
            quantity = float(request.POST['quantity'])
            cho0 = int(request.POST['cho0'])
            cho = int(request.POST['cho'])
            cho1 = int(request.POST['cho1'])
            cho2 = int(request.POST['cho2'])
            cho3 = int(request.POST['cho3'])
            cho4 = int(request.POST['cho4'])
            cho5 = int(request.POST['cho5'])
            cho6 = int(request.POST['cho6'])
            cho7 = int(request.POST['cho7'])
            cho8 = int(request.POST['cho8'])
            cho9 = int(request.POST['cho9'])
            cho11 = int(request.POST['cho11'])
            cho12 = int(request.POST['cho12'])
            cho13 = int(request.POST['cho13'])
            cho14 = int(request.POST['cho14'])
        else:
            return render(request, 'result-early-diagnosis.html', {'result':'Something went wrong'})

        #result = predictions.getPredictions(int(request.GET['quantity']),int(request.GET['cho0']),int(request.GET['cho']),int(request.GET['cho1']),int(request.GET['cho2']),int(request.GET['cho3']),int(request.GET['cho4']),int(request.GET['cho5']),int(request.GET['cho6']),int(request.GET['cho7']),int(request.GET['cho8']),int(request.GET['cho9']),int(request.GET['cho11']),int(request.GET['cho12']),int(request.GET['cho13']),int(request.GET['cho14']))
        result = predictions.getPredictions(quantity,cho,cho0,cho1,cho2,cho3,cho4,cho5,cho6,cho7,cho8,cho9,cho11,cho12,cho13,cho14)
        if (result == "You don't have diabetes"):
            message = "We're happy to inform you that "
        else:
            message = "We're sad to inform you that"
        
        #print(quantity,cho,cho0,cho1,cho2,cho3,cho4,cho5,cho6,cho7,cho8,cho9,cho11,cho12,cho13,cho14)
        #print("result:::::",result)
        return render(request, 'result-early-diagnosis.html', {'result':result,'message':message})







# the sign up or registration function
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User = get_user_model()
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'sign-up.html', {'error_message': 'Username already exists.'})
        elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return render(request, 'sign-up.html', {'error_message': 'Email already exists.'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('signin')
    else:
        return render(request, 'sign-up.html')

# the login function
def signin(request):
    if request.method == 'POST':
        #login is done by entering username not email
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'sign-in.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'sign-in.html')
    

# the logout function
def logoutuser(request):
    logout(request)
    return redirect('/')

def faqs(request):
    return render(request,'faqs.html')

def foodpoints(request):
    return render(request,'food-points.html')

def steps(request):
    return render(request,'steps.html')

def chatbot(request):
    return render(request,'chatbot.html')








# arabic views

@login_required(login_url='signin-ar')
def scanar(request):
    message = ""
    prediction = ""
    fss = CustomFileSystemStorage()
    try:
        image = request.FILES["image"]
        print("Name", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" + image.name
        # image details
        image_url = fss.url(_image)
        # Read the image
        imag=cv2.imread(path)
        imag1 = cv2.resize(imag,(300,300))
        X = np.array((imag1[np.newaxis])/255)

        # load model
        model = tf.keras.models.load_model(os.getcwd() + '/dumbs/densenet_bestqwk.h5')
        score_predict=((model.predict(X).ravel()*model.predict(X[:, ::-1, :, :]).ravel()*model.predict(X[:, ::-1, ::-1, :]).ravel()*model.predict(X[:, :, ::-1, :]).ravel())**0.25).tolist()
        label_predict = np.argmax(score_predict)

        # ----------------
        # LABELS
        # 0 - No diabetic retinopathy
        # 1 - Mild
        # 2 - Moderate
        # 3 - Severe
        # 4 - Proliferative diabetic retinopathy
        # ----------------

        
        prediction = label_predict
        print("improtant::  "+str(label_predict))
        if (prediction == 0):
            prediction = "ليس لديك اعتلال الشبكية السكري"
            message = "نحن سعداء جدا من أجلك"
        elif (prediction == 1):
            prediction = "اعتلال الشبكية السكري خفيف"
            message = "نحن آسفون من أجلك"
        elif (prediction == 2):
             prediction = "اعتلال الشبكية السكري لديك متوسط"
             message = "نحن آسفون من أجلك"
        elif (prediction == 3):
             prediction = "اعتلال الشبكية السكري لديك شديد"
             message = "نحن آسفون من أجلك"
        elif (prediction == 4):
             prediction = "اعتلال الشبكية السكري الخاص بك منتشر بكثرة"
             message = "نحن آسفون من أجلك"
        else:
             prediction = "حدث خطأ ما"
        
         
        
        return TemplateResponse(
            request,
            "arabic/result-retin.html",
            {
                "message": message,
                "image": image,
                "image_url": image_url,
                "prediction": prediction,
            },
        )
    except MultiValueDictKeyError:

        return TemplateResponse(
            request,
            "arabic/retin-scan-fe.html",
            {"message": "لم يتم تحديد صورة"},
        )

def homear(request):
    return render(request,'arabic/index.html')

@login_required(login_url='signin-ar')
def earlydiagnosisar(request):
    return render(request,'arabic/early-diagnosis.html')
    

    """ This code does the following:
1. Takes the input from the form
2. Passes the input to the model
3. Renders the result and a message """

def resultar(request):
        if request.method == 'POST':
            quantity = float(request.POST['quantity'])
            cho0 = int(request.POST['cho0'])
            cho = int(request.POST['cho'])
            cho1 = int(request.POST['cho1'])
            cho2 = int(request.POST['cho2'])
            cho3 = int(request.POST['cho3'])
            cho4 = int(request.POST['cho4'])
            cho5 = int(request.POST['cho5'])
            cho6 = int(request.POST['cho6'])
            cho7 = int(request.POST['cho7'])
            cho8 = int(request.POST['cho8'])
            cho9 = int(request.POST['cho9'])
            cho11 = int(request.POST['cho11'])
            cho12 = int(request.POST['cho12'])
            cho13 = int(request.POST['cho13'])
            cho14 = int(request.POST['cho14'])
        else:
            return render(request, 'arabic/result-early-diagnosis.html', {'result':'هناك خطأ ما'})

        #result = predictions.getPredictions(int(request.GET['quantity']),int(request.GET['cho0']),int(request.GET['cho']),int(request.GET['cho1']),int(request.GET['cho2']),int(request.GET['cho3']),int(request.GET['cho4']),int(request.GET['cho5']),int(request.GET['cho6']),int(request.GET['cho7']),int(request.GET['cho8']),int(request.GET['cho9']),int(request.GET['cho11']),int(request.GET['cho12']),int(request.GET['cho13']),int(request.GET['cho14']))
        result = predictions.getPredictions(quantity,cho,cho0,cho1,cho2,cho3,cho4,cho5,cho6,cho7,cho8,cho9,cho11,cho12,cho13,cho14)
        if (result == "You don't have diabetes"):
            message = "يسعدنا إبلاغك بأن ليس لديك مرض السكري "
        else:
            message = "يحزننا إخبارك بأن لديك مرض السكري"
        
        #print(quantity,cho,cho0,cho1,cho2,cho3,cho4,cho5,cho6,cho7,cho8,cho9,cho11,cho12,cho13,cho14)
        #print("result:::::",result)
        return render(request, 'arabic/result-early-diagnosis.html', {'result':result,'message':message})







# the sign up or registration function
def signupar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User = get_user_model()
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'arabic/sign-up.html', {'error_message': 'اسم المستخدم موجود بالفعل'})
        elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return render(request, 'arabic/sign-up.html', {'error_message': 'البريد الالكتروني موجود بالفعل.'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('signin-ar')
    else:
        return render(request, 'arabic/sign-up.html')

# the login function
def signinar(request):
    if request.method == 'POST':
        #login is done by entering username not email
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/ar')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'arabic/sign-in.html', {'error': 'خطأ في اسم المستخدم أو كلمة مرور'})
    else:
        return render(request, 'arabic/sign-in.html')
    

# the logout function
def logoutuserar(request):
    logout(request)
    return redirect('/ar')

def faqsar(request):
    return render(request,'arabic/faqs.html')

def foodpointsar(request):
    return render(request,'arabic/food-points.html')

def stepsar(request):
    return render(request,'arabic/steps.html')

def chatbotar(request):
    return render(request,'arabic/chatbot.html')

