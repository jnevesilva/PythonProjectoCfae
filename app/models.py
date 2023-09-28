from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User


ACAO_CHOICES=(
    ('CS', 'Curso'),
    ('OF', 'Oficina'),
    ('ACD', 'Ação de Curta Duração'),
    ('CE', 'Circulo de Estudos'))

DOC_CHOICES=(
    ('CC', 'Cartão de Cidadão'), 
    ('PP', 'Passaporte'),
    ('CR', 'Certificado de Residência'))

HAB_CHOICES=(
    ('DR', 'Doutoramento'), 
    ('MR', 'Mestrado'),
    ('LC', 'Licenciatura'))

GRUPO_CHOICES=(
    ('100', 'Educação Pré-Escolar'),
    ('110', '1º Ciclo'),
    ('120', 'Inglês'),
    ('550', 'Informática'), 
    
    )

ESCALAO_CHOICES=(
    ('1º', '1º Escalão'),
    ('2º', '2º Escalão'), 
    ('3º', '3º Escalão'),
    ('4º', '4º Escalão'),
    ('5º', '5º Escalão'),
    ('6º', '6º Escalão'),
    ('7º', '7º Escalão'),
    ('8º', '8º Escalão'),
    ('9º', '9º Escalão'),
    ('10º','10º Escalão'))

INDICE_CHOICES=(
    ('120º', '120'),
    ('130', '130'),
    ('240', '240'),
    ('500', '500'))

NIVEL_CHOICES=(
    ('PE', 'Pré- Escolar'), 
    ('1C', '1º ciclo'),
    ('2C', '2º ciclo'),
    ('3C', '3º ciclo'),
    ('SC', 'Secundário'),
    ('EE', 'Educação Especial'))

VINCULO_CHOICES=(
    ('QE', 'Quadro de Escola'),
    ('QZP', 'Quadro de zona'),
    ('CNT', 'Contratado'))

AGRUPAMENTO_CHOICES=(
    ('AEAS', 'Agrupamento de Escolas Abel Salazar'),
    ('AEPOL', 'Agrupamento de Escolas Prof. Óscar Lopes'),
    ('ESAG', 'Escola Secundária Auguto Gomes'),
    ('ZARCO', 'Escola Secundária João Gonçalves Zarco'),
    ('ESAG', 'Escola SEcundária Augusto Gomes'),
    ('ESBN', 'Escola secundária da Boa Nova'),
    ('AEP', 'Agrupamento de Escolas de Perafita'),
    ('AESH', 'Agrupamento de Escolas da Senhora da Hora'),
    ('AEFPO', 'Agrupamento de Escolas Fernando Pinto de Oliveira'),
    ('AEJDS', 'Agrupamento de Escolas José Domigues dos Santos'),
    ('AEIP', 'Agrupamento de Escolas de Irmãos Passos'),
    ('AESH', 'Agrupamento de Escolas da Senhora da Hora',))

REGIME_CHOICES=(
    ('O', 'Online'),
    ('P', 'Presencial'),
    ('H', 'Híbrido'))


class Acao(models.Model):
    codigo = models.CharField('Código da Ação', max_length=20)
    designacao = models.CharField('Designação da Ação', max_length=100)
    modalidade = models.CharField('Modalidade', max_length=3, choices=ACAO_CHOICES) 
    horas = models.IntegerField('Número de horas da ação', null=True)
    caducidade = models.DateField()
    registo = models.CharField('Número de Registo', max_length=40)
    acao_images = models.ImageField(upload_to='images')
    acao_doc = models.URLField('Descritivo da ação', default="http://cfaematosinhos.eu")

    def __str__(self):
        return self.designacao
    

class Docente(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField('Tipo de utilizador', max_length=20)
    nome = models.CharField('Nome', max_length=100)
    nascimento = models.DateField('data de nascimento')
    genero = models.CharField('Género', max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    nacionalidade = models.CharField('Nacionalidade', max_length=30, default='Portuguesa')
    identificacao = models.CharField('Documento de identificação', max_length=2,choices=DOC_CHOICES)
    numeroid = models.CharField('Número do Cartão', max_length=20)
    validadeid = models.DateField('Data de Validade')
    nif = models.CharField('NIF', max_length=10)
    niss = models.CharField('NISS', max_length=10)
    habilitacoes = models.CharField('Habilitações Literárias', max_length=25, choices=HAB_CHOICES)
    endereco = models.CharField('Endereço', max_length=60)
    codigopostal = models.CharField('Código Postal', max_length=8)
    localidade = models.CharField('Localidade', max_length=30)
    telemovel = models.CharField('Telemóvel', max_length=12)
    telefone = models.CharField('Telefone', max_length=12)
    datainiciofuncoes = models.DateField('Data início de funções', null=True)
    grupo = models.CharField('Grupo Disciplinar', max_length=3, null=True, choices=GRUPO_CHOICES)
    escalao = models.CharField('Escalão', max_length=3, null=True, choices=ESCALAO_CHOICES)
    proximaprogressao = models.DateField('Data da próxima progressão', null=True)
    indice = models.CharField('Indice', max_length=4, null=True, choices=INDICE_CHOICES)
    nivel = models.CharField('nivel de ensino',max_length=4, choices=NIVEL_CHOICES, default='SC')
    vinculo= models.CharField('nivel de ensino', max_length=4,choices=VINCULO_CHOICES, default='QE')
    agrupamento= models.CharField('nivel de ensino',max_length=5, choices=AGRUPAMENTO_CHOICES, default='ZARCO')
    formador = models.BooleanField("formador", default=False)
  

    def __str__(self):
        return self.nome


class Turma(models.Model):
    codigoacao = models.ForeignKey(Acao, blank=True, null=True, on_delete=models.CASCADE)
    turma = models.CharField('Turma', max_length=15, blank=True, null=True)
    datainicio = models.DateField()
    datafim = models.DateField()
    regime = models.CharField('Regime de frequência', max_length=4, null=True, choices=REGIME_CHOICES)
    publicoalvo = models.CharField("publico alvo", max_length=80, null=True, default="Professores do ensino básico e secundário")
    datainicioinsc = models.DateField('datainicioinscricao', default="2023-01-01")
    datalimiteinsc = models.DateField('datalimteinscricao', default="2023-01-01")
    fechada = models.BooleanField('Fechada', default=False)


    def __str__(self):
        return str(self.turma) 


class Sessoes(models.Model):
    codturma = models.ForeignKey(Turma, blank=True, null=True, on_delete=models.CASCADE)
    sessao = models.IntegerField()
    data = models.DateField()
    hora = models.TimeField()
    duracao = models.FloatField()
    localformacao = models.CharField('localformacao', max_length=50, blank=True, default="")
    sumario = models.TextField('localformacao', max_length=400, blank=True, default="")
    faltas = models.ManyToManyField(Docente)

    def __str__(self):
        return str(self.sessao)


class Inscritos(models.Model):
    idturma = models.ForeignKey(Turma, blank=True, null=True, on_delete=models.CASCADE)
    idutilizador = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    datahorainscricao = models.DateTimeField()
    confirmado = models.BooleanField('Confirma frequência', default=False)
    concluiu = models.BooleanField('concluiu a ação', default=False)
    classificacao = models.FloatField("Classificação", default=0)
    formador = models.BooleanField("formador", default=False)
    
    class Meta:
        unique_together = ('idturma', 'idutilizador')

    def __int__(self):
        return self.idturma
    
