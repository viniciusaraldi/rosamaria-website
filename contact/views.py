from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    send = False
    
    form = ContactForm(request.POST or None)
    if form.is_valid():
        #enviar e-mail
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        title = request.POST.get('title','')
        message = request.POST.get('message','')
        email = EmailMessage(
            "Mensagem do Blog Django",
            "De {}\nE-mail: <{}> \nEscreveu: \n\nTitulo: {}\nAssunto:\n{}".format(name,email,title,message),
            "nao-responder@inbox.mailtrap.io",
            ["viniciusheckert14@gmail.com"],
            reply_to=[email]
        )
        try:
            email.send()
            send = True
        except:
            send = False       
    
    context = {
        'form':form,
        'success':send,
    }
    return render(request,'contact/contact.html',context)    


    """
        nome = forms.CharField(label="Nome", widget=forms.TextInput(attrs={'placeholder':'Digite seu nome'}))
    email = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'placeholder':'Digite seu e-mail'}))
    mensagem = forms.CharField(label="Assunto", widget=forms.Textarea(attrs={'placeholder':'Digite o assunto'}))
    """