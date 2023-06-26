from django.shortcuts import render
from django.http import HttpResponse
import hashlib
import sys
import os
from .forms import *
from .aes_methods import *



def home(request):
    

    encryptionForm = EncryptionForm(request.POST or None)
    decryptionForm = DecryptionForm(request.POST or None)
    text = None
    cipher = None

    if encryptionForm.is_valid():
        
        key = encryptionForm.cleaned_data['key']
        text = encryptionForm.cleaned_data['text']
        
        
        iv = os.urandom(16)
       
        
        hash = hashlib.sha3_256()
        hash.update(str.encode(key))     
                
        
        cipher = encrypt(hash.hexdigest(),text, iv)
        iv = base64.b64encode(iv).decode()
        
        
        
        
        context = {
            'encryptionForm': encryptionForm,
            'decryptionForm' : decryptionForm,
            'cipher': cipher,
            'iv' : iv,
            'encryptionMode' : True,
            
        }
        return render(request, 'home.html', context)
    
    

    if decryptionForm.is_valid():
        key = decryptionForm.cleaned_data['key']
        cipher = decryptionForm.cleaned_data['cipher']
        iv = decryptionForm.cleaned_data['iv']
        
        
       # print(iv)
       
        
        hash = hashlib.sha3_256()
        hash.update(str.encode(key))                    
        
        try:
            plainText = decrypt(hash.hexdigest(),cipher,iv)
        except:
            plainText = cipher

        context = {
            'encryptionForm': encryptionForm,
            'decryptionForm' : decryptionForm,
            'text': plainText,                        
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
