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
from Filmes import views
from django.contrib.auth import views as auth_views
app_name = "Filmes"
urlpatterns = [
path('cria/', views.FilmeReviewCreate.as_view(),name='cria-review'),
path('lista/', views.FilmeList.as_view(),name='lista-review'),
path('atualiza/<int:pk>/',views.FilmeReviewUpdate.as_view(),name='atualiza-review'),
path('apaga/<int:pk>/',views.FilmeReviewDelete.as_view(),name='apaga-review'),
path('', views.FilmeList.as_view(),name='home-review'),
]