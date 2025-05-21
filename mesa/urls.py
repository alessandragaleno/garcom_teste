from django.urls import path
from . import views

urlpatterns = [
    
    path('gerar_qr_code/<int:mesa_id>/', views.gerar_qr_code, name='gerar_qr_code'),
    path('ocupar_mesa/<int:mesa_id>/', views.ocupar_mesa, name='ocupar_mesa'),
    path('desocupar_mesa/<int:mesa_id>/', views.desocupar_mesa, name='desocupar_mesa'),
]

