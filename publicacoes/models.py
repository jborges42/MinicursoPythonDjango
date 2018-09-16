from django.db import models

class Categoria(models.Model):
	nome = models.CharField(max_length=100)
	dt_criaco = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.nome

class Publicacao(models.Model):
	titulo = models.CharField(max_length=100)
	descricao = models.TextField()
	dt_criaco = models.DateField(auto_now_add=True)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'Publicações'
		
	def __str__(self):
		return self.titulo