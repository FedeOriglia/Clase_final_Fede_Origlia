"""mtv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function viewsp
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ejemplo_soft.views import index, PostList, PostCrear
from ejemplo_soft.views import (index, PostDetalle, PostListar, PostCrear,
                               PostBorrar, PostActualizar, UserSignUp, UserLogin,
                               UserLogout, AvatarActualizar, UserActualizar,
                               MensajeCrear, MensajeListar, MensajeDetalle, About)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ejemplo-soft/', index, name="ejemplo-soft-index"),
    path('ejemplo-soft/listar/', PostList.as_view(), name="ejemplo-soft-listar"),
    path('ejemplo-soft/<int:pk>/detalle/', PostDetalle.as_view(), name="ejemplo-soft-detalle"),
    path('ejemplo-soft/listar/', PostListar.as_view(), name="ejemplo-soft-listar"),
    path('ejemplo-soft/crear/', PostCrear.as_view(), name="ejemplo-soft-crear"),
    path('ejemplo-soft/<int:pk>/borrar/', PostBorrar.as_view(), name="ejemplo-soft-borrar"),
    path('ejemplo-soft/<int:pk>/actualizar/', PostActualizar.as_view(), name="ejemplo-soft-actualizar"),
    path('ejemplo-soft/signup/', UserSignUp.as_view(), name="ejemplo-soft-signup"),
    path('ejemplo-soft/login/', UserLogin.as_view(), name="ejemplo-soft-login"),
    path('ejemplo-soft/logout/', UserLogout.as_view(), name="ejemplo-soft-logout"),
    path('ejemplo-soft/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="ejemplo-soft-avatars-actualizar"),
    path('ejemplo-soft/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="ejemplo-soft-users-actualizar"),
    path('ejemplo-soft/mensajes/crear/', MensajeCrear.as_view(), name="ejemplo-soft-mensajes-crear"),
    path('ejemplo-soft/mensajes/listar/', MensajeListar.as_view(), name="ejemplo-soft-mensajes-listar"),
    path('ejemplo-soft/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="ejemplo-soft-mensajes-detalle"),
    path('ejemplo-soft/about/', About, name="ejemplo-soft-about"),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)