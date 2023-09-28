from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordResetForm
from django.contrib.auth.models import User
from .models import Docente, Sessoes


class Loginform(AuthenticationForm):
    username =UsernameField(label='Utilizador', widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    password=forms.CharField(label='Palavra-passe', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class CustomerRegistrationForm(UserCreationForm):
    username =forms.CharField(label='Utilizador', widget=forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    email=forms.EmailField(label='Correiro eletrónico', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1=forms.CharField(label='Palavra-passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2=forms.CharField(label='Confirme palavra-passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields=['username', 'email', 'password1', 'password2']


class MyPasswordResetForm(PasswordResetForm):
    pass


class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = "__all__" 
        labels = {
                'username': '',
                'tipo': 'Tipo de utilizador',
                'nome': 'Nome completo',
                'nascimento':'Data de nascimento',
                'genero':'Género',
                'nacionalidade':'Nacionalidade',
                'identificacao': 'Tipo de documento de identificação',
                'numeroid': 'Número de documento',
                'validadeid':'Data de validade',
                'nif': 'NIF',
                'niss':'NISS',
                'habilitacoes': 'Habilitações literárias',
                'endereco': 'Endereço',
                'codigopostal': 'Código postal',
                'localidade': 'Localidade',
                'telemovel': 'Telemóvel',
                'telefone': 'Telefone',
                'datainiciofuncoes': 'Data início de funções',
                'escalao': 'Escalão',
                'proximaprogressao': 'Data de próxima progressão',
                'indice': 'Índice',
                'nivel': 'Nivel',
                'vinculo': 'Vinculo',
                'agrupamento': 'Agrupamento',
                'formador': 'Formador'
        }
        
        widgets={
            
                'username': forms.Select(attrs={'class':'form-control', 'hidden':True }),
                'tipo': forms.TextInput(attrs={'class':'form-control'}),
                'nome': forms.TextInput(attrs={'class':'form-control'}),
                'nascimento': forms.widgets.DateInput(attrs={'type': 'date' }),
                'genero': forms.Select(attrs={'class':'form-control'}),
                'nacionalidade': forms.TextInput(attrs={'class':'form-control'}),
                'identificacao': forms.Select(attrs={'class':'form-control'}),
                'numeroid': forms.TextInput(attrs={'class':'form-control'}),
                'validadeid': forms.widgets.DateInput(attrs={'type': 'date' }),
                'nif': forms.TextInput(attrs={'class':'form-control'}),
                'niss': forms.TextInput(attrs={'class':'form-control'}),  
                'habilitacoes': forms.Select(attrs={'class':'form-control'}),  
                'endereco': forms.TextInput(attrs={'class':'form-control'}),  
                'codigopostal': forms.TextInput(attrs={'class':'form-control'}),  
                'localidade': forms.TextInput(attrs={'class':'form-control'}),  
                'telemovel': forms.TextInput(attrs={'class':'form-control'}),  
                'telefone': forms.TextInput(attrs={'class':'form-control'}), 
                'datainiciofuncoes': forms.widgets.DateInput(attrs={'type': 'date'}),
                'grupo': forms.Select(attrs={'class':'form-control'}),
                'escalao': forms.Select(attrs={'class':'form-control'}), 
                'proximaprogressao': forms.widgets.DateInput(attrs={'type': 'date'}),
                'indice': forms.Select(attrs={'class':'form-control'}), 
                'nivel': forms.Select(attrs={'class':'form-control'}), 
                'vinculo': forms.Select(attrs={'class':'form-control'}), 
                'agrupamento': forms.Select(attrs={'class':'form-control'}),  
                'formador': forms.CheckboxInput       
        }



class CriarSessoesForm(forms.ModelForm):
    
    class Meta:

        model = Sessoes
        fields = "__all__" 
      
        labels = {
            "codturma":"",
            "sessao":"nº da sessao",
            "data":"Data",
            "hora":"Hora",
            "duracao":"Duracao",
            "localformacao":"Local da formacao",
            "sumario":"Sumario",
            "faltas":"Faltas(prima CTRL ou CMD para várias)",
        }

        widgets={
            
                'codturma': forms.TextInput(attrs={'class':'form-control', 'hidden':True }),
                'sessao': forms.NumberInput(attrs={'class':'form-control'}),
                'data': forms.widgets.DateInput(attrs={'type': 'date'}),
                'hora':  forms.TimeInput(attrs={'type': 'time','class':'form-control',}),
                'duracao': forms.NumberInput(attrs={'class':'form-control',}),
                'localformacao': forms.TextInput(attrs={'class':'form-control',}),
                'sumario': forms.Textarea(attrs={'class':'form-control', }), 
                'faltas': forms.SelectMultiple(attrs={'class':'form-control',}),
                
             }

class AtualizarSessaoForm(forms.ModelForm):
    
    class Meta:

        model = Sessoes
        fields = "__all__" 
        labels = {
            "codturma":"",
            "sessao":"nº da sessao",
            "data":"Data",
            "hora":"Hora",
            "duracao":"Duracao",
            "localformacao":"Local da formacao",
            "sumario":"Sumario",
            "faltas":"Faltas(prima CTRL ou CMD para várias)",
        }

        widgets={
            
                'codturma': forms.TextInput(attrs={'class':'form-control', 'hidden':True }),
                'sessao': forms.NumberInput(attrs={'class':'form-control'}),
                'data': forms.widgets.DateInput(attrs={'type': 'date'}),
                'hora':  forms.TimeInput(attrs={'type': 'time','class':'form-control',}),
                'duracao': forms.NumberInput(attrs={'class':'form-control',}),
                'localformacao': forms.TextInput(attrs={'class':'form-control',}),
                'sumario': forms.Textarea(attrs={'class':'form-control', }),
                'faltas': forms.SelectMultiple(attrs={'class':'form-control', }),
                
             }