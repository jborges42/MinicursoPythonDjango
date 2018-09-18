from django.shortcuts import render, redirect
from .models import Publicacao
from .form import PublicacaoForm

def home(request):
	data={}
	data['publicacoes'] = Publicacao.objects.all()
	return render(request, 'publicacoes/home.html', data)

def novaPublicacao(request):
	data={}
	form = PublicacaoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('url_home')

	data['form'] = form
	return render(request, 'publicacoes/formulario.html', data )

def editaPublicacao(request, id):
	data = {}
	posts = Publicacao.objects.get(id=id)

	form = PublicacaoForm(request.POST or None, instance=posts)
	if form.is_valid():
		form.save()
		return redirect('url_home')

	data['form'] = form

	return render(request, 'publicacoes/formulario.html', data)

def deletaPublicacao(request, id):
	posts = Publicacao.objects.get(id=id)
	posts.delete()
	return redirect('url_home')	

def post(request, id):
	data = {}
	posts = Publicacao.objects.get(id=id)
	data['publicacoes'] = Publicacao.objects.all()

	return render(request, 'publicacoes/post.html', data)