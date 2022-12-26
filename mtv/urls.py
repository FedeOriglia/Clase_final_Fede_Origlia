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
from ejemplo.views import (mostrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar, FamiliarDetalle)
from ejemplo_dos.views import index, PostList, PostCrear
from ejemplo_dos.views import (index, PostDetalle, PostListar, PostCrear,
                               PostBorrar, PostActualizar, UserSignUp, UserLogin,
                               UserLogout, AvatarActualizar, UserActualizar,
                               MensajeCrear, MensajeListar, MensajeDetalle, About)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi-familia/', mostrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('panel-familia/', FamiliarList.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('panel-familia/crear', FamiliarCrear.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('ejemplo-dos/', index, name="ejemplo-dos-index"),
    path('ejemplo-dos/listar/', PostList.as_view(), name="ejemplo-dos-listar"),
    path('ejemplo-dos/<int:pk>/detalle/', PostDetalle.as_view(), name="ejemplo-dos-detalle"),
    path('ejemplo-dos/listar/', PostListar.as_view(), name="ejemplo-dos-listar"),
    path('ejemplo-dos/crear/', PostCrear.as_view(), name="ejemplo-dos-crear"),
    path('ejemplo-dos/<int:pk>/borrar/', PostBorrar.as_view(), name="ejemplo-dos-borrar"),
    path('ejemplo-dos/<int:pk>/actualizar/', PostActualizar.as_view(), name="ejemplo-dos-actualizar"),
    path('ejemplo-dos/signup/', UserSignUp.as_view(), name="ejemplo-dos-signup"),
    path('ejemplo-dos/login/', UserLogin.as_view(), name="ejemplo-dos-login"),
    path('ejemplo-dos/logout/', UserLogout.as_view(), name="ejemplo-dos-logout"),
    path('ejemplo-dos/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="ejemplo-dos-avatars-actualizar"),
    path('ejemplo-dos/users/<int:pk>/actualizar/', UserActualizar.as_view(), name="ejemplo-dos-users-actualizar"),
    path('ejemplo-dos/mensajes/crear/', MensajeCrear.as_view(), name="ejemplo-dos-mensajes-crear"),
    path('ejemplo-dos/mensajes/listar/', MensajeListar.as_view(), name="ejemplo-dos-mensajes-listar"),
    path('ejemplo-dos/mensajes/<int:pk>/detalle/', MensajeDetalle.as_view(), name="ejemplo-dos-mensajes-detalle"),
    path('ejemplo-dos/about/', About, name="ejemplo-dos-about"),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)