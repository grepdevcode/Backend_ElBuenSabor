from django.shortcuts import render
from .models import RubroArticulo, Articulo, ArticuloManufacturado
from rest_framework import viewsets
from .serializers import RubroArticuloSerializer, ArticuloSerializer, ArticuloManufacturadoSerializer
from rest_framework import generics

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import text
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict

from django.http import HttpResponse



class RubroArticuloViewSet(generics.ListCreateAPIView):

    queryset = RubroArticulo.objects.all()
    serializer_class = RubroArticuloSerializer


class RubroArticuloSetDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = RubroArticulo.objects.all()
    serializer_class = RubroArticuloSerializer


class ArticuloViewSet(generics.ListCreateAPIView):

    queryset = Articulo.objects.all()
    #print("This: ",queryset)
    serializer_class = ArticuloSerializer


class ArticuloSetDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Articulo.objects.all()
    ##print(queryset)
    serializer_class = ArticuloSerializer



class ArticuloManufacturadoViewSet(generics.ListCreateAPIView):

    queryset = ArticuloManufacturado.objects.all()
    serializer_class = ArticuloManufacturadoSerializer


class ArticuloManufacturadoSetDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = ArticuloManufacturado.objects.all()
    serializer_class = ArticuloManufacturadoSerializer

def greeting(self):

    engine = create_engine('postgresql+pygresql://postgres:123@localhost:5432/elbuensabor2', echo=True)
    meta = MetaData()
    meta.bind = engine
    conn = engine.connect()
    artt = Table("Articulos_articulo", meta, autoload=True)
    #s = artt.select()
    s = artt.select().join()
    t = text('select "Articulos_articulo".denominacion, "Articulos_rubroarticulo".denominacion from "Articulos_articulo" inner join "Articulos_rubroarticulo" on "Articulos_articulo"."rubroArticulo_id" = "Articulos_rubroarticulo".id')
    t2 = text('select "Articulos_articulo".denominacion from "Articulos_articulo"')
    t3 = text('select "Articulos_articulo"."precioCompra" from "Articulos_articulo"')
    result = conn.execute(t)
    lista = []

    for res in result:
    	print(res)
    	lista.append(res)


	#model_instance = YourModel.object.first()
    #model_dict = model_to_dict(result)

	#json.dumps(model_dict, cls=DjangoJSONEncoder)
    #>>>>Works!!!return HttpResponse(json.dumps([str(r) for r in result]))
    #>>>>>Works!return HttpResponse(json.dumps([list(r) for r in result]))
    #return json.dumps(model_dict, cls=DjangoJSONEncoder)
    return HttpResponse(json.dumps([list(r) for r in lista]))
