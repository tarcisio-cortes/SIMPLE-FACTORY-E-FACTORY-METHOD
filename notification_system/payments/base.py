# Classes de Pagamento (Product)
from abc import ABC, abstractmethod

class Pagamento(ABC):
    """
    [Product Abstrato] Interface base para todos os métodos de pagamento.
    Define o contrato para executar o pagamento.
    """

    def __init__(self, valor: float):
        """Inicializa o método de pagamento com o valor a ser pago."""
        self.valor = valor

    @abstractmethod
    def pagar(self):
        """
        Método abstrato para processar o pagamento.
        As subclasses concretas devem implementá-lo com a lógica de pagamento específica.
        """
        pass

class PagamentoCartaoCredito(Pagamento):
    """[Produto Concreto] Implementação de pagamento via Cartão de Crédito."""
    def pagar(self):
        """Processa o pagamento simulado via Cartão de Crédito."""
        print(f"💳 Processando R$ {self.valor:.2f} via Cartão de Crédito...")
        print("   Status: Transação aprovada e concluída.")

class PagamentoPix(Pagamento):
    """[Produto Concreto] Implementação de pagamento via PIX."""
    def pagar(self):
        """Processa o pagamento simulado via PIX."""
        print(f"📲 Gerando código PIX para R$ {self.valor:.2f}...")
        print("   Status: Pagamento instantâneo aguardando confirmação.")

class PagamentoBoleto(Pagamento):
    """[Produto Concreto] Implementação de pagamento via Boleto Bancário."""
    def pagar(self):
        """Processa o pagamento simulado via Boleto."""
        print(f"📄 Gerando Boleto Bancário para R$ {self.valor:.2f}...")
        print("   Status: Boleto gerado. Vencimento em 3 dias úteis.")