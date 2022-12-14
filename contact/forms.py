from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder':'Nome','class':'special1'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Telefone','class':'special2'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'E-mail','class':'special3'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Assunto','class':'special4'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Coloque sua mensagem aqui!','class':'special5'}))