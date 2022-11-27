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
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from ExemplosWeb.views import homepage, homeSec , registro, secreto,MeuUpdateView
from django.contrib.auth.views import LoginView , LogoutView
from django.urls.base import reverse_lazy
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User





urlpatterns = [
    path('admin/', admin.site.urls),
    path("contatos/", include ('contatos.urls')),
    path('',homepage,name = 'tela-inicial'),
    path('accounts/',homeSec,name='sec-home'),
    path('accounts/registro/',registro, name = 'sec-registro'),
    path('accounts/login/',LoginView.as_view(template_name='registro/login.html'),name = 'sec-login'),
    path('secreto/',secreto, name='sec-secreta'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('sec-login'),), name='sec-logout'),
    path('accounts/password_change/',PasswordChangeView.as_view(template_name='registro/password_change_form.html',success_url=reverse_lazy('sec-password_change_done'),), name = 'sec-troca-senha'),
    path('accounts/senhaTrocada/',PasswordChangeDoneView.as_view(template_name='registro/password_change_done'), name = 'sec-senha-trocada'),
    path('accounts/terminaRegistro/<int:pk>/',MeuUpdateView.as_view(template_name='registro/user_form.html',success_url=reverse_lazy('sec-home'),model=User,fields=['first_name','last_name','email',],), name='sec-termina-registro'),

]
