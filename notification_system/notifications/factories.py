# Factories Abstratas e Concretas (Factory Method/Abstract Factory)
from abc import ABC, abstractmethod
from .base import (
    Notificacao, 
    NotificacaoEmail, 
    NotificacaoSMS, 
    NotificacaoWhatsApp
)

# Fábrica Abstrata (Abstract Factory)
class NotificacaoFactory(ABC):
    """
    Define o método de criação (Factory Method) que as fábricas concretas devem implementar.
    A descrição do problema sugere uma Abstract Factory que 'contém' um Factory Method.
    """

    @abstractmethod
    def criarNotificacao(self, destino: str, mensagem: str) -> Notificacao:
        """Método Factory Method para criar um objeto Notificacao."""
        pass

# Fábrica Concreta 1: Prioriza canais rápidos (SMS ou WhatsApp)
class FactoryNotificacaoUrgente(NotificacaoFactory):
    """Fábrica que prioriza a criação de NotificacaoSMS ou WhatsApp."""
    
    def criarNotificacao(self, destino: str, mensagem: str) -> Notificacao:
        # Lógica de priorização para urgência: usa SMS
        print("🚨 Usando fábrica URGEGENTE. Priorizando SMS.")
        return NotificacaoSMS(destino, mensagem)

# Fábrica Concreta 2: Usa canais padrão (e-mail)
class FactoryNotificacaoNormal(NotificacaoFactory):
    """Fábrica que utiliza o canal padrão, como E-mail."""

    def criarNotificacao(self, destino: str, mensagem: str) -> Notificacao:
        # Lógica padrão: usa E-mail
        print("🗓️ Usando fábrica NORMAL. Usando E-mail.")
        return NotificacaoEmail(destino, mensagem)