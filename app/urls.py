from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import Loginform, MyPasswordResetForm

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home),
    path('registo/', views.CustomerRegistrationView.as_view(), name='registoutilizador'),
    path('profile/', views.profile, name='profile'),
    path('turmas/', views.TurmasView.as_view(), name='turmas'),
    path('turmasinscricoes/', views.TurmasInscricoesView.as_view(), name='turmasinscricoes'),

    path('acao/', views.AcoesView.as_view(), name='acao'),
    path('turmas/inscricao_detalhe/<int:pk>', views.InscricaoDetailView.as_view(), name='inscricao'),
    path('turmas/inscricao_detalhe/confirma/<int:pk>', views.add_insc, name='inscricaoconfirma'),
    path('listauserinscricao', views.lista_user_inscricao, name='inscricaouser'),
    path('listainscritos', views.InscricaoView.as_view(), name='listainscritos'),
    path('deleteuserinscricao/<int:inscricao_id>', views.delete_user_inscricao, name='deleteuserinscricao'),
    
    #Lista inscritos na turma
    path('turmas/turma_inscritos/<str:pk>/', views.turma_inscritos, name='turmainscritos'),
    path('turmas/gestao_inscricoes/', views.gestao_inscricoes, name='gestao_inscricoes'),

    path('turmas/turma_inscritos_pdf/<str:pk>/', views.turma_inscritos_pdf, name='turma_inscritos_pdf'),
    
    #User autentications
    path ('accounts/login/', auth_view.LoginView.as_view(template_name='login.html', authentication_form=Loginform), name='login'),
    path ('accounts/logout/', auth_view.LogoutView.as_view(), name='logout'),
    path ('accounts/password-reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path ('criar_sessao/<int:turma>',views.criar_registo, name="criar_sessao"),
    path ('atualizar_sessao/<int:pk>',views.atualizar_registo, name="atualizar_sessao"),
    path ('apagar_registo/<int:pk>',views.apagar_registo, name="apagar_registo"),

    path ('calendas/',views.CalendasView.as_view(), name="calendas"),
    path ('calendas/<int:sort>',views.calendas, name="calendas"),

    path ('gerapdf',views.some_view, name="gerapdf"), 

   
]
