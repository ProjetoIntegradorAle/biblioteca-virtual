import datetime
from .models import FraseDoDia 

def frase_do_dia(request):
    dias = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
    hoje = dias[datetime.datetime.today().weekday()]
    frase = FraseDoDia.objects.filter(dia_semana=hoje).first()
    return {'frase_do_dia': frase}

