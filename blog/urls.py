"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from publicacoes.views import home, novaPublicacao, editaPublicacao, deletaPublicacao, post

from publicacoes.views import home, novaPublicacao, editaPublicacao, deletaPublicacao


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('post/<int:id>/', post, name='url_post'),
    path('nova/', novaPublicacao, name='url_nova'),
    path('editar/<int:id>/', editaPublicacao, name='url_editar'),
    path('deleta/<int:id>/', deletaPublicacao, name='deletar')

]
