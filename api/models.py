from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField("Nome do Criador", max_length=150)
    biografia = models.CharField("Biografia do jogador", max_length=350, null=True, blank=True)
    pontos = models.IntegerField("Pontos do jogador", default=0)

    def __str__(self):
        return "{} - @{}".format(self.nome, self.user.username)


class Jogo(models.Model):
    nome = models.CharField("Nome do Jogo", max_length=150)
    resumo = models.CharField("Descrição do Jogo", max_length=350)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    html = models.TextField("HTML", max_length=10000, null=True, blank=True)
    css = models.TextField("CSS", max_length=10000, null=True, blank=True)
    js = models.TextField("JS", max_length=10000, null=True, blank=True)

    def __str__(self):
        return "{} jogo de {}".format(self.nome, self.autor.nome)


class Seguidor(models.Model):
    class Meta:
        verbose_name = "Seguidor"
        verbose_name_plural = "Seguidores"
        
    usuario = models.ForeignKey(Usuario, related_name="quem_segue", on_delete=models.CASCADE)
    segue = models.ForeignKey(Usuario, related_name="sendo_seguido", on_delete=models.CASCADE)

    def __str__(self):
        return "[{}] segue [{}]".format(self.usuario.nome, self.segue.nome)
    

class Like(models.Model):
    usuario = models.ForeignKey(Usuario, related_name="quem_curtiu", on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)

    def __str__(self):
        return "{} curitu o jogo {}".format(self.usuario.nome, self.jogo.nome)
    

