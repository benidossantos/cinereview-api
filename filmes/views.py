from django.http import JsonResponse
from .models import Filme, Avaliacao
from django.db.models import Avg

def listar_filmes(request):
    filmes = Filme.objects.all()
    dados = []

    for filme in filmes:
        media = Avaliacao.objects.filter(filme=filme).aggregate(Avg('nota'))
        dados.append({
            "id": filme.id,
            "titulo": filme.titulo,
            "genero": filme.genero,
            "ano_lancamento": filme.ano_lancamento,
            "media_avaliacoes": media['nota__avg']
        })

    return JsonResponse(dados, safe=False)


def listar_filmes_bem_avaliados(request):
    filmes = Filme.objects.all()
    dados = []

    for filme in filmes:
        media = Avaliacao.objects.filter(filme=filme).aggregate(Avg('nota'))
        if media['nota__avg'] and media['nota__avg'] >= 4:
            dados.append({
                "id": filme.id,
                "titulo": filme.titulo,
                "media_avaliacoes": media['nota__avg']
            })

    return JsonResponse(dados, safe=False)
