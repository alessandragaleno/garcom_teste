from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.html, name='home'),
    path('mesa/<int:mesa_id>/', views.detalhes_mesa, name='detalhes_mesa'),
    path('gerar_qr_code/<int:mesa_id>/', views.gerar_qr_code, name='gerar_qr_code'),
    path('ocupar_mesa/<int:mesa_id>/', views.ocupar_mesa, name='ocupar_mesa'),
]

