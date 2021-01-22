from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [

   path('index', views.index, name='index'),
   path('impresoras', views.impresoras, name='impresoras'),
   path('mouse', views.mouse, name='mouse'),
   path('teclados', views.teclados, name='teclados'),
   path('crud_alumno', views.crud_alumno, name='crud_alumno'),
   path('agregar_alumno', views.agregar_alumno, name='agregar_alumno'),
   path('form_editar/<int:pk>', views.form_editar, name='form_editar'),
   path('form_eliminar/<int:pk>', views.form_eliminar, name='form_eliminar'),
   path('actualizar', views.actualizar, name='actualizar'),
   path('eliminar', views.eliminar, name='eliminar'),
]
