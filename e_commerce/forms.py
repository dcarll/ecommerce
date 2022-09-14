import email
from django import forms

class ContatoForm(forms.Form):
    nome_completo = forms.CharField(
    error_messages={'required': 'Obrigatório o preenchimento do nome'},
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Seu nome completo"
                }
            )
        )
    email     = forms.EmailField(
        error_messages={'invalid': 'Digite um email válido!'},
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite seu email"
                }
            )
        )
    mensagem   = forms.CharField(
        error_messages={'required': 'É obrigatório o preenchimento do campo mensagem!'},
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua mensagem"
                }
            )
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("o email dever ser do gmail")
        return email

