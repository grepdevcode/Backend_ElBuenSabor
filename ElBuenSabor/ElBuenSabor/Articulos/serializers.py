from .models import RubroArticulo
from .models import Articulo
from .models import ArticuloManufacturado
from rest_framework import serializers


class RubroArticuloSerializer(serializers.HyperlinkedModelSerializer):
    #arts = serializers.StringRelatedField(many=True)

    class Meta:
        model = RubroArticulo
        fields = ('id', 'denominacion')


class ArticuloSerializer(serializers.HyperlinkedModelSerializer):
	#url = serializers.HyperlinkedIdentityField(view_name="artdetail:articulo-detail")
    
    #rubroArticulo = RubroArticulo.arts

    #rubroArticulo1 = RubroArticuloSerializer(many=True)
    #rubroArticulo=serializers.HyperlinkedRelatedField(
         #view_name='rubroarticulo-detail', lookup_field='pk', read_only=True)
    rubroArticulo = serializers.PrimaryKeyRelatedField(read_only=True)
    #print(rubroArticulo)
    #rubroArticulo = serializers.StringRelatedField()
    #print("aaaaaaaaa",rubroArticulo)
    #print(a)
    #print(Articulo.rubroArticulo.id)
	
    #checked_objects = Articulo.objects.all()
    #print("---",checked_objects)
    #checked_objects = Articulo.objects.all()
    #a = list(checked_objects)
    
    
    	
    #for checked_object in checked_objects.all():
    #	for i in checked_object:
    #        print(">>>>>>>>>>>>>>>>>>><<", i)

    	

    	#for i in enumerate(checked_object):
            #print(">>	",checked_object)
    #a = [Articulo.objects.get(rubroArticulo)]
    #print(a)

    #for i in enumerate(a):
     #   print(i[1])
    #rubroArticulo = serializers.HyperlinkedRelatedField(
     #   many=True, view_name='RubroArticulo-detail', lookup_field='denominacion', read_only=True)

    #arts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    """
    rubroArticulo = serializers.HyperlinkedRelatedField(
        view_name='RubroArticuloSetDetail',
        lookup_field = 'denominacion',
        read_only=True)
	"""
    r = "hello"
    #rubroArticulo = serializers.RelatedField(many=True)

    class Meta:
        model = Articulo
        fields = ['url', 'id', 'denominacion', 'precioCompra', 'precioVenta',
                  'stockActual', 'unidadDeMedida', 'esInsumo', 'rubroArticulo']
        

    # fields = ('__all__')


class ArticuloManufacturadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticuloManufacturado
        fields = ('id', 'tiempoEstimadoCocina', 'denominacion', 'precioVenta')
