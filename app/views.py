from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View, generic
from django.utils import timezone
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import CustomerRegistrationForm, DocenteForm, CriarSessoesForm, AtualizarSessaoForm
from .models import Docente, Turma, Acao, Inscritos, Sessoes 
from datetime import date,datetime


from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse, FileResponse
import io


# Create your views here.
def home(request):
    return render(request, 'home.html')
    

class CustomerRegistrationView(View):
    def get(self, request):
        form=CustomerRegistrationForm()
        return render(request, 'customerregistration.html', locals())
    def post(self, request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Parabéns, está registado")
        else:
            messages.warning(request, "Dados inválidos")
        return render(request, 'customerregistration.html', locals())
    
    
#criar o perfil opção 1)
def profile(request):
    if (Docente.objects.filter(username=request.user)):
        docente=Docente.objects.get(username=request.user)
        if (request.method=='POST'):
            form=DocenteForm(request.POST, instance=docente)     
            if form.is_valid():
                form.save()
                messages.success(request, "Os seus dados foram gravados com sucesso")
            else:
                messages.warning(request, "Dados inválidos")

        form=DocenteForm (initial={'username': request.user}, instance=docente)
        return render(request, 'profile.html',{'form': form})
    else:
        if (request.method=='POST'):
            form=DocenteForm(request.POST)     
            if form.is_valid():
                form.save()
                messages.success(request, "Os seus dados foram gravados com sucesso")
            else:
                messages.warning(request, "Dádos inválidos")
        form=DocenteForm (initial={'username': request.user})
        return render(request, 'profile.html',{'form': form})


#criar o perfil opção 2)
class ProfileView(View):
    def get(self, request):
        docente=Docente.objects.get(username=request.user).id
        form = DocenteForm({'username': request.user}, instance=docente)
        return render(request, 'profile.html',{'form': form})
     

    def post(self, request):
        form = DocenteForm(request.POST)
        if form.is_valid():
            username=request.user
            tipo=form.cleaned_data['tipo']
            nome=form.cleaned_data['nome']
            nascimento=form.cleaned_data['nascimento']
            genero=form.cleaned_data['genero']
            nacionalidade=form.cleaned_data['nacionalidade']
            identificacao=form.cleaned_data['identificacao']
            numeroid=form.cleaned_data['numeroid']
            validadeid=form.cleaned_data['validadeid']
            nif=form.cleaned_data['nif']
            niss=form.cleaned_data['niss']
            habilitacoes=form.cleaned_data['habilitacoes']
            endereco=form.cleaned_data['endereco']
            codigopostal=form.cleaned_data['codigopostal']
            localidade=form.cleaned_data['localidade']
            telemovel=form.cleaned_data['telemovel']
            telefone=form.cleaned_data['telefone']
            datainiciofuncoes=form.cleaned_data['datainiciofuncoes']
            grupo=form.cleaned_data['grupo']
            escalao=form.cleaned_data['escalao']
            proximaprogressao=form.cleaned_data['proximaprogressao']
            indice=form.cleaned_data['indice']
            nivel = form.cleaned_data['nivel']
            vinculo = form.cleaned_data['vinculo']
            agrupamento = form.cleaned_data['agrupamento']
            formador = form.cleaned_data['formador']


            reg = Docente(username=username, nascimento=nascimento,tipo=tipo, nome=nome, genero=genero, nacionalidade=nacionalidade,
                          validadeid=validadeid, identificacao=identificacao, numeroid=numeroid, nif=nif, niss=niss,
                            habilitacoes=habilitacoes,endereco=endereco, codigopostal=codigopostal, localidade=localidade,
                            telemovel=telemovel, telefone=telefone, datainiciofuncoes=datainiciofuncoes, grupo=grupo, escalao=escalao,
                            proximaprogressao=proximaprogressao, indice=indice,nivel=nivel, vinculo=vinculo, 
                            agrupamento=agrupamento, formador=formador )
            reg.save()
            messages.success(request, "Os seus dados foram gravados com sucesso")
        else:
            messages.warning(request, "Dádos inválidos")

        return render(request, 'profile.html',locals())
    
    
class TurmasView(generic.ListView):
    model = Turma
    context_object_name = 'turmas_list'
    queryset = Turma.objects.all().order_by('-datainicio')
    template_name = 'turmas.html'


class TurmasInscricoesView(generic.ListView):
    model = Turma
    context_object_name = 'turmas_list'
    queryset = Turma.objects.all()
    template_name = 'turmasinscricoes.html'


class AcoesView(generic.ListView):
    model = Acao
    context_object_name = 'acao_list'
    queryset = Acao.objects.all()
    template_name = 'listaacoes.html'


class InscricaoDetailView(generic.DetailView):
    model = Turma
    context_object_name = 'idetalhe'
    template_name = 'inscricao_detalhe.html'      


# registar inscrição
def add_insc(request, pk):
        user = request.user
        q1 = Inscritos.objects.filter(idutilizador=user)
        q2 = q1.filter(idturma=pk)
        if (not q2):
            Inscritos(idutilizador=user, idturma_id=pk,datahorainscricao = timezone.datetime.now()).save()
        return redirect("/turmas")


# lista de inscrições do formando
def lista_user_inscricao(request):
    user = request.user
    insc=Inscritos.objects.filter(idutilizador=user)
    formador = Inscritos.objects.filter(idutilizador=user).filter(formador=True)
    tot_insc=Inscritos.objects.all()
    return render(request, 'listauserinscricao.html', locals())


def delete_user_inscricao(request, inscricao_id):
    inscricao=Inscritos.objects.get(pk=inscricao_id)
    inscricao.delete()
    return redirect ('/listauserinscricao')


# lista de inscritos
class InscricaoView(generic.ListView):
    model = Inscritos
    context_object_name = 'inscritos_list'
    queryset = Inscritos.objects.all().order_by('idturma')
    template_name = 'listainscritos.html'


# lista de inscritos na turma
def turma_inscritos(request, pk):
    inscritos=Inscritos.objects.filter(idturma=pk)
    turma = Turma.objects.get(id=pk)
    
    #turma = inscritos[0].idturma
    listaturmas=Turma.objects.all().filter(fechada=False)
    listadocentes = Docente.objects.all().order_by("agrupamento", "nome")
    listaformadores = Docente.objects.filter(formador=True).order_by("agrupamento", "nome")
    return render(request, 'turmainscritos.html', locals())


##GESTÃO DE INSCRIÇÔES - MOVER PARA OUTRA TURMA  ###############################
def gestao_inscricoes(request):
    
    if request.method == 'POST':
        if 'mover' in request.POST:
            check = request.POST.getlist("checks[]")
            check_turma=request.POST.get('turma')
            for i in check:
                try:
                    b = Inscritos.objects.get(pk=i)
                    b_turma = Turma.objects.get(turma=check_turma)
                    b.idturma=b_turma 
                    b.save()
                except IntegrityError as e: 
                    if 'unique constraint' in e.args:
                        continue 

        if 'inscrever' in request.POST:
            turma_atual = request.POST.get("turma_atual")
            turmaobj = Turma.objects.get(turma=turma_atual)
            docente_check = request.POST.get("docente")
            docenteobj= Docente.objects.get(id=docente_check).id
            q1 = Inscritos.objects.filter(idutilizador=docenteobj)
            q2 = q1.filter(idturma=turmaobj)
            if (not q2):
                Inscritos(idutilizador_id=docenteobj, idturma=turmaobj,
                        datahorainscricao = timezone.datetime.now()).save()
            
        if 'associar' in request.POST:
            turma_atual = request.POST.get("turma_atual")
            turmaobj = Turma.objects.get(turma=turma_atual)
            docente_check = request.POST.get("formador")
            docenteobj= Docente.objects.get(id=docente_check).id
            q1 = Inscritos.objects.filter(idutilizador=docenteobj)
            q2 = q1.filter(idturma=turmaobj)
            if (not q2):
                Inscritos(idutilizador_id=docenteobj, idturma=turmaobj,
                    datahorainscricao = timezone.datetime.now(), formador=True).save()
  
        if 'eliminar' in request.POST:
            check = request.POST.getlist("checks[]")
            #check_turma=request.POST.get('turma')
            for i in check:
                try:
                    b = Inscritos.objects.get(pk=i)
                    b.delete()
                except IntegrityError as e: 
                    if 'unique constraint' in e.args:
                        continue 

        if 'confirmar' in request.POST:
            check = request.POST.getlist("checks[]")
            #check_turma=request.POST.get('turma')
            for i in check:
                b = Inscritos.objects.get(pk=i)
                if b.confirmado:
                    b.confirmado=False
                else:
                    b.confirmado=True
                b.save()
                

        return redirect(request.META['HTTP_REFERER'])


# lista de inscritos na turma - PDF ######################
def turma_inscritos_pdf(request, pk):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4, bottomup=0)
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 12)
    inscritos=Inscritos.objects.filter(idturma=pk)
    if (inscritos):
        turma = inscritos[0].idturma
    lines =[]
    lines.append("Centro de formação da XPTO - Matosinhos  ")
    lines.append("")
    lines.append("Ação: " + turma.codigoacao.designacao)
    lines.append("Turma: " + turma.turma)
    lines.append("--------------------------------")
    for inscrito in inscritos:
        lines.append(inscrito.idutilizador.username + "   " + inscrito.idutilizador.docente.nome + "   " + inscrito.idutilizador.docente.grupo + "  " + inscrito.idutilizador.docente.agrupamento)
      
    for line in lines:
        textobj.textLine(line)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True)


# criar uma sessão ###################################
@login_required(login_url='login.html')
def criar_registo(request,turma):

    form = CriarSessoesForm()
    if request.method == "POST":
        form=CriarSessoesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inscricaouser")
    else:
        proxsessao=Sessoes.objects.filter(codturma=turma).count()+1
        form=CriarSessoesForm(initial={
            'codturma':turma,
            'sessao':proxsessao,})
    context = {'form':form}
    return render(request, 'criar-sessao.html', context=context)


@login_required(login_url='login.html')
def atualizar_registo(request,pk):
    registo=Sessoes.objects.get(id=pk)
    form=AtualizarSessaoForm(instance=registo)
    if request.method == 'POST':
        form=AtualizarSessaoForm(request.POST, instance=registo)
        if form.is_valid():
            form.save()
            return redirect("inscricaouser") 
    context = {'form':form}
    return render(request, 'atualizar-sessao.html', context=context)


@login_required(login_url='login.html')
def apagar_registo(request, pk):
    registo=Sessoes.objects.get(id=pk)
    registo.delete()
    return redirect ('inscricaouser')


class CalendasView(generic.ListView):
    model = Sessoes
    context_object_name = 'calendas'
    queryset = Sessoes.objects.all().order_by('data', 'hora')
    template_name = 'calendas.html'

def calendas(request,sort):
    if sort==1:
        queryset=Sessoes.objects.all().order_by('-data','-hora')
    else:
        if sort==2:
            queryset=Sessoes.objects.all().order_by('data', 'hora')
        else:
            if sort==3:
                queryset=Sessoes.objects.all().order_by('codturma','data' )
            else:
                if sort==4:
                    queryset=Sessoes.objects.all().order_by('-codturma', 'data')

    context = {
        'calendas': queryset
    }
    return render(request,"calendas.html",context)



##TESTE PARA CRIAÇÂO DE PDF  ############################################
def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(1, 1, "Hello world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response