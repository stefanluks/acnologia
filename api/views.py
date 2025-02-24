from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Jogo, Like, Seguidor, Usuario

# Create your views here.
def Main(request):
    return JsonResponse(data={"erro":False}, safe=False)

def GetQtdLikes(request, id_jogo):
    if Jogo.objects.filter(pk=id_jogo):
        jogo = Jogo.objects.get(pk=id_jogo)
        cont = len(list(Like.objects.filter(pk=id_jogo)))
        return JsonResponse(data={
            "error":False,
            "jogo":jogo.pk,
            "nome_jogo":jogo.nome,
            "qtd_likes":cont,
        })
    else:
        return JsonResponse(data={
            "error":True,
            "msg":"Jogo não encontrado!"
        })


def GetLikes(request, id_jogo):
    if Jogo.objects.filter(pk=id_jogo):
        jogo = Jogo.objects.get(pk=id_jogo)
        cont = len(list(Like.objects.filter(pk=id_jogo)))
        obj = {
            "error":False,
            "jogo":jogo.pk,
            "nome_jogo":jogo.nome,
            "qtd_likes":cont,
            "quem_curtiu":[]
        }
        for l in list(Like.objects.filter(pk=id_jogo)):
            json = {"id":l.id, "usuario":{"id":l.usuario.id, "nome":l.usuario.nome}}
            obj["quem_curtiu"].append(json)
        return JsonResponse(data=obj, safe=False)
    else:
        return JsonResponse(data={
            "error":True,
            "msg":"Jogo não encontrado!"
        }, safe=False)