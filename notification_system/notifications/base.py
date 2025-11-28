# Classes de Notificação (Hierarquia)
from abc import ABC, abstractmethod

# Classe base Abstrata
class Notificacao(ABC):
    """Classe base abstrata para todos os tipos de notificação."""

    def __init__(self, destino: str, mensagem: str):
        self.destino = destino
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self):
        """Método abstrato que deve ser implementado pelas subclasses."""
        pass

# Subclasses Concretas
class NotificacaoEmail(Notificacao):
    """Notificação por E-mail."""
    def enviar(self):
        print(f"📧 Enviando E-mail para: {self.destino}")
        print(f"   Mensagem: {self.mensagem}")

class NotificacaoSMS(Notificacao):
    """Notificação por SMS."""
    def enviar(self):
        print(f"📱 Enviando SMS para: {self.destino}")
        print(f"   Mensagem: {self.mensagem}")

class NotificacaoWhatsApp(Notificacao):
    """Notificação por WhatsApp."""
    def enviar(self):
        print(f"💬 Enviando WhatsApp para: {self.destino}")
        print(f"   Mensagem: {self.mensagem}")
