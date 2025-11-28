# Cliente (Serviço de Notificação)
from .base import Notificacao
from .factories import NotificacaoFactory

class ServicoNotificacao:
    """
    O Cliente do padrão Factory Method. 
    Ele depende da NotificacaoFactory abstrata, não das fábricas concretas.
    """

    def __init__(self, factory: NotificacaoFactory):
        """O cliente recebe a fábrica no construtor (Injeção de Dependência)."""
        self._factory = factory

    def notificar(self, destino: str, mensagem: str):
        """Usa a fábrica para criar e enviar a notificação."""
        print("-" * 30)
        # O cliente usa o Factory Method para criar a notificação
        notificacao = self._factory.criarNotificacao(destino, mensagem)
        
        # O cliente usa o objeto, sem saber sua classe concreta
        notificacao.enviar()
        print("-" * 30)