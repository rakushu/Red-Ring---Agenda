"""contactos URL Configuration

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
from django.urls import path, include

from contactbook.views import contact_detail_page, contact_update_page, contact_delete_page, contact_create_page, contact_list_page

from .views import home_page

from usuarioalta.views import signup

urlpatterns = [
    #Vista admin
    path('admin/', admin.site.urls),

    #Vista principal
    path('', home_page, name='home'),

    #Vista signup
    path('unete/', signup, name='signup'),

    #Vista login-logout
    path('cuenta/', include('django.contrib.auth.urls')),

    #Vista contactos
    path('contactos/', contact_list_page, name='list_contacts'),

    #Vista detalle contactos
    path('contactos/detalles/<int:contact_id>/', contact_detail_page, name='details'),

    #Vista añadir contacto
    path('contactos/agregar/', contact_create_page, name='add'),

    #Vista actualizar contacto
    path('contactos/actualizar/<int:contact_id>/', contact_update_page, name='update'),

    #Vista borrar contacto
    path('contactos/borrar/<int:contact_id>/', contact_delete_page, name='delete'),


]
