"""ElBuenSabor URL Configuration

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
"""
from django.contrib import admin
from django.urls import path 
#from ElBuenSabor.Articulos.views import articulosManufacturados
#from ElBuenSabor.usuarios.api import PersonaResource


urlpatterns = [

    path('admin/', admin.site.urls),
    #path('Articulos/fechayhora/',current_datetime),
    #path('Articulos/articulosmanufacturados/',articulosManufacturados),

]"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from ElBuenSabor.usuarios import views
from ElBuenSabor.Articulos import views as viewsarticulo
#from ElBuenSabor.Articulos import greeting
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url

#router = routers.DefaultRouter()
#router.register(r'cliente', views.UserViewSet)
#router.register(r'cliente/<int:pk>/', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'articulo/<int:pk>/', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = format_suffix_patterns([

    #    #path('clientes/', views.cliente_list),
    #    #path('clientes/<int:pk>/', views.cliente_detail),
    #path('admin/', admin.site.urls),
    #path(r'^',include(viewsarticulo.ArticuloViewSet.as_view())),
    #path(r'^',include(viewsarticulo.ArticuloSetDetail.as_view())),
    #path('', include(router.urls)),
    
    #path('', views.api_root),
    
    path('clientes/', views.UserViewSet.as_view()),
    path('clientes/<int:pk>/', views.UserViewSetDetail.as_view()),
    path('rubroarticulo/', viewsarticulo.RubroArticuloViewSet.as_view()),
    path('rubroarticulo/<int:pk>/', viewsarticulo.RubroArticuloSetDetail.as_view()),
    path('articulo/', viewsarticulo.ArticuloViewSet.as_view(), name='articulo-list'),
    path('articulo/<int:pk>/', viewsarticulo.ArticuloSetDetail.as_view(), name='articulo-detail'),
    path('articulomanufacturado/', viewsarticulo.ArticuloManufacturadoViewSet.as_view()),
    path('articulomanufacturado/<int:pk>/',
         viewsarticulo.ArticuloManufacturadoSetDetail.as_view()),
    url(r'^greetings/$', viewsarticulo.greeting),
    #    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    

])


#urlpatterns = format_suffix_patterns(urlpatterns)
