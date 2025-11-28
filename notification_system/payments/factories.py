# Factories de Pagamento (Creator)
from abc import ABC, abstractmethod
from .base import Pagamento, PagamentoCartaoCredito, PagamentoPix, PagamentoBoleto

class PagamentoFactory(ABC):
    """
    [Creator Abstrato] Define a interface para o Factory Method de criação de Pagamentos.
    O cliente (Serviço) usará apenas esta interface.
    """

    @abstractmethod
    def criarPagamento(self, valor: float) -> Pagamento:
        """
        O Factory Method. 
        As subclasses concretas implementam para criar um Pagamento Concreto.
        """
        pass
        
    def processar(self, valor: float):
        """
        Método que usa o Factory Method para criar e operar o produto.
        Esta é uma lógica padrão que o Creator pode ter.
        """
        print("-" * 30)
        print(f"Iniciando serviço de pagamento para valor: R$ {valor:.2f}")
        
        # Uso do Factory Method: a criação do produto está desacoplada
        pagamento = self.criarPagamento(valor)
        
        # Execução da operação (pagar())
        pagamento.pagar()
        print("-" * 30)


class FactoryPagamentoRapido(PagamentoFactory):
    """
    [Creator Concreto] Fábrica para pagamentos rápidos (Cartão ou PIX). Prioriza Cartão.
    """
    def criarPagamento(self, valor: float) -> Pagamento:
        """Cria e retorna um objeto PagamentoCartaoCredito."""
        print("⚡ Usando fábrica RÁPIDA. Priorizando Cartão de Crédito.")
        return PagamentoCartaoCredito(valor)

class FactoryPagamentoPrazo(PagamentoFactory):
    """
    [Creator Concreto] Fábrica para pagamentos com prazo (Boleto).
    """
    def criarPagamento(self, valor: float) -> Pagamento:
        """Cria e retorna um objeto PagamentoBoleto."""
        print("🐌 Usando fábrica PRAZO. Usando Boleto.")
        return PagamentoBoleto(valor)