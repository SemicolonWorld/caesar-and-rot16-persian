from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,

)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import EncryptAndDecryptModel
from extensions.algorithm import Encrypt, Decrypt
enc = Encrypt()
dec = Decrypt()

# Create your views here.
    
def caesar(request):
    if request.method == 'POST':
        encordec = request.POST.get('encordec').lower()
        text = request.POST.get('text')
        if encordec == 'encrypt':
            result = enc.caesar(text)
            obj = EncryptAndDecryptModel.objects.create(
                text = text,
                result = result,
                encordec = 'e',
                what_type = 'c'
            )
            obj.save()
            data = {
                'text': text,
                'result': result,
                'encordec': encordec,
            }
            return render(request, 'metcrypt/caesar.html', context = data)
        elif encordec == 'decrypt':
            result = dec.caesar(text)
            obj = EncryptAndDecryptModel.objects.create(
                text = text,
                result = result,
                encordec = 'd',
                what_type = 'c'
            )
            obj.save()
            data = {
                'text': text,
                'result': result,
                'encordec': encordec,
            }
            return render(request, 'metcrypt/caesar.html', context = data)
    
    return render(request, 'metcrypt/caesar.html')

def rot16(request):
    if request.method == 'POST':
        encordec = request.POST.get('encordec').lower()
        text = request.POST.get('text')
        if encordec == 'encrypt':
            result = enc.rot16(text)
            obj = EncryptAndDecryptModel.objects.create(
                text=text,
                result=result,
                encordec='e',
                what_type='r'
            )
            obj.save()
            data={
                'text': text,
                'result': result,
                'encordec': encordec
            }
            return render(request, 'metcrypt/rot16.html', context = data)
        elif encordec == 'decrypt':
            result = dec.rot16(text)
            obj = EncryptAndDecryptModel.objects.create(
                text=text,
                result=result,
                encordec='d',
                what_type='r'
            )
            obj.save()
            data={
                'text': text,
                'result': result,
                'encordec': encordec
            }
            return render(request, 'metcrypt/rot16.html', context = data)
    return render(request, 'metcrypt/rot16.html')



def home(request):
    return render(request, 'metcrypt/index.html')