"""ExemplosWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls.conf import path
from contatos import views
app_name = "contatos"
urlpatterns = [
path('cria/', views.ContatoCreateView.as_view(),name='cria-contato'),
path('lista/', views.ContatoListView.as_view(),name='lista-contatos'),
path('atualiza/<int:pk>/',views.ContatoUpdateView.as_view(),name='atualiza-contato'),
path('apaga/<int:pk>/',views.ContatoDeleteView.as_view(),name='apaga-contato'),
path('', views.ContatoListView.as_view(),name='home-contatos'),
]