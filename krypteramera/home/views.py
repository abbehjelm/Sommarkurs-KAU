from django.shortcuts import render
from django.http import HttpResponse
import hashlib
import sys
from .forms import *
from .aes_methods import *


def home(request):
    encrypt('Nyckel', "En massa text En massa text")


    encryptionForm = EncryptionForm(request.POST or None)
    decryptionForm = DecryptionForm(request.POST or None)
    text = None
    cipher = None

    if encryptionForm.is_valid():
        
        key = encryptionForm.cleaned_data['key']
        iv = encryptionForm.cleaned_data['iv']
        text = encryptionForm.cleaned_data['text']
        
        print(iv)
       
        
        hash = hashlib.sha3_256()
        hash.update(str.encode(key))     
        
        iv_hash = hashlib.sha3_256()
        iv_hash.update(str.encode(iv)) 
        
        
        context = {
            'encryptionForm': encryptionForm,
            'decryptionForm' : decryptionForm,
            'cipher': text,
            'encryptionMode' : True,
            
        }
        return render(request, 'home.html', context)
    
    

    if decryptionForm.is_valid():
        key = decryptionForm.cleaned_data['key']
        cipher = decryptionForm.cleaned_data['cipher']

        context = {
            'encryptionForm': encryptionForm,
            'decryptionForm' : decryptionForm,
            'text': cipher,
            'encryptionMode' : False,
        }
        return render(request, 'home.html', context)


    context = {
        'encryptionForm': encryptionForm,
        'decryptionForm' : decryptionForm,
        'encryptionMode' : True,
        'cipher': cipher,
        'text': text,
    }
    return render(request, 'home.html', context)
