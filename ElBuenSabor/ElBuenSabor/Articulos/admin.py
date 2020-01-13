from django.contrib import admin
from .models import RubroArticulo
from .models import Articulo
from .models import ArticuloManufacturado
from .models import ArticuloManufacturadoDetalle
from .models import DetallePedido
# Register your models here.
admin.site.register(RubroArticulo)
admin.site.register(Articulo)
admin.site.register(ArticuloManufacturado)
admin.site.register(ArticuloManufacturadoDetalle)
admin.site.register(DetallePedido)
