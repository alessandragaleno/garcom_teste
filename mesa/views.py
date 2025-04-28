from django.utils import timezone
from django.shortcuts import render
import qrcode
from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import get_object_or_404
from .models import Mesa

def gerar_qr_code(request, mesa_id):
    mesa = get_object_or_404(Mesa, id=mesa_id)  # noqa: F841
    
    # URL que será embutida no QR Code
    url = 'http://localhost:8000/mesa/1/'  # Ajuste conforme sua URL

    # Gera o QR Code
    qr = qrcode.make(url)

    # Salva o QR Code em um objeto BytesIO para exibir na resposta HTTP
    img_io = BytesIO()
    qr.save(img_io)
    img_io.seek(0)

    # Retorna o QR Code como imagem
    return HttpResponse(img_io, content_type="image/png")


# Create your views here.
def home(request):
    return render(request, 'home.html')

def ocupar(self, cliente):
        """Método para marcar a mesa como ocupada e associar um cliente"""
        self.status = 'ocupada'
        self.cliente = cliente
        self.data_ocupacao = timezone.now()  # noqa: F821
        self.save()

def desocupar(self):
    """Método para liberar a mesa"""
    self.status = 'disponivel'
    self.cliente = None
    self.data_ocupacao = None
    self.save()

def is_disponivel(self):
    """Método para verificar se a mesa está disponível"""
    return self.status == 'disponivel'

